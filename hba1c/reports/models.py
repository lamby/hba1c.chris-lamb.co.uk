import datetime

from django_yadt import YADTImageField

from django.db import models

class PreviewImage(models.Model):
    session = models.ForeignKey(
        'session.Session',
        related_name='preview_images',
    )

    image = YADTImageField(
        filename_prefix=lambda x: '%s_%d' % (x.session.slug, x.order),
    )

    order = models.IntegerField()

    created = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        ordering = ('order',)
        unique_together = (
            ('session', 'order'),
        )

    def delete(self):
        super(PreviewImage, self).delete()

        self.image.delete()
