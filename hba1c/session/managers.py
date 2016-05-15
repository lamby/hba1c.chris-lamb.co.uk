import time
import random
import hashlib
import datetime

from django.db import models
from django.conf import settings
from django.shortcuts import redirect

from .enums import StageEnum

class SessionManager(models.Manager):
    def session_namespace(self):
        return '%s.%s.session_key' % (
            self.model._meta.app_label,
            self.model._meta.object_name,
        )

    def get_for(self, request):
        try:
            return self.model.objects.get(
                session_key=request.session[self.session_namespace()],
            )
        except (KeyError, self.model.DoesNotExist):
            return None

    def clear_for(self, request):
        request.session.pop(self.session_namespace())

    def set_for(self, request, **kwargs):
        namespace = self.session_namespace()

        try:
            session_key = request.session[namespace]
        except KeyError:
            session_key = hashlib.sha1('%s%s%s' % (
                random.randrange(0, 2 << 63),
                time.time(),
                settings.SECRET_KEY,
            )).hexdigest()

            request.session[namespace] = session_key

        session, created = self.model.objects.get_or_create(
            session_key=session_key,
        )

        if not created:
            kwargs['updated'] = datetime.datetime.utcnow()

            try:
                # Ratchet stage by only updating it if we don't have one
                # greater than it.
                if kwargs['stage'] <= session.stage:
                    kwargs.pop('stage', None)
            except KeyError:
                pass

            for k, v in kwargs.iteritems():
                setattr(session, k, v)

            session.save(update_fields=kwargs.keys())

        return session, created

    def set_and_redirect(self, request, stage, **kwargs):
        self.set_for(request, stage=stage, **kwargs)

        return redirect(StageEnum.urlconf(stage))
