import datetime

from django.db import models

class Result(models.Model):
    session = models.ForeignKey(
        'session.Session',
        related_name='results',
    )

    date = models.DateField()
    value = models.IntegerField()

    created = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        ordering = ('date',)
        get_latest_by = 'created'
        unique_together = (
            ('session', 'date'),
        )

    def __unicode__(self):
        return u"pk=%d date=%r value=%d" % (
            self.pk,
            self.date,
            self.value,
        )
