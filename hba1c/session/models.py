import datetime

from django_enumfield import enum

from django.db import models
from django.utils.crypto import get_random_string

from .enums import StageEnum
from .managers import SessionManager

class Session(models.Model):
    session_key = models.CharField(max_length=40, unique=True)

    name = models.CharField(max_length=150)

    slug = models.CharField(
        unique=True,
        max_length=12,
        default=get_random_string,
    )

    stage = enum.EnumField(StageEnum)

    # Are we currently generating a PDF?
    generating_pdf = models.BooleanField(default=False)

    updated = models.DateTimeField(default=datetime.datetime.utcnow)
    created = models.DateTimeField(default=datetime.datetime.utcnow)

    objects = SessionManager()

    def __unicode__(self):
        return u"%s" % self.slug
