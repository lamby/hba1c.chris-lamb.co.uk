import functools

from django.http import HttpResponseBadRequest
from django.shortcuts import redirect

from .models import Session

class funnel_stage(object):
    def __init__(self, stage, fallback=None):
        self.stage = stage
        self.fallback = fallback

    def __call__(self, fn, *args, **kwargs):
        @functools.wraps(fn)
        def wrapper(request, *args, **kwargs):
            if self.fallback:
                session = Session.objects.get_for(request)

                if not session or session.stage < self.stage:
                    if request.is_ajax():
                        return HttpResponseBadRequest(
                            "Session has not reached this stage"
                        )

                    return redirect(self.fallback)

            session, created = Session.objects.set_for(
                request,
                stage=self.stage,
            )

            # If we just created a session and we have a querystring, strip it
            # off.
            if created and request.method == 'GET' and request.GET and \
                    not request.is_ajax():
                return redirect(request.path)

            try:
                return fn(request, session, *args, **kwargs)
            finally:
                # Delete the session if it was a bot. Removing it afterwards
                # means the view can alwaya assume it has a session.
                user_agent = request.META.get('HTTP_USER_AGENT', '')

                for x in (
                    "KeyError.com uptime check",
                    "Twitterbot/",
                    "TweetmemeBot/",
                    "AhrefsBot/",
                    "MetaURI API/",
                    "NING/",
                    "Baiduspider/",
                ):
                    if x in user_agent and created:
                        session.delete()
                        break

        return wrapper
