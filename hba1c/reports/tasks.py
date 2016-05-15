import os
import shutil
import tempfile
import cStringIO
import subprocess

from celery import shared_task

from django.core.files.base import File
from django.core.files.storage import default_storage

from hba1c.session.models import Session

from .utils import render_pdf

@shared_task()
def generate_pdf_and_previews(slug):
    session = Session.objects.get(slug=slug)

    filename = '%s.pdf' % session.slug

    fileobj = cStringIO.StringIO()
    render_pdf(session, fileobj)

    # Ensure we delete any existing one so we don't get {{ slug }}_1.pdf, etc.
    default_storage.delete(filename)

    assert default_storage.save(filename, fileobj) == filename, \
        "Not stored at the location we requested"

    try:
        tempdir = tempfile.mkdtemp()

        src = os.path.join(tempdir, filename)
        with open(src, 'w') as f:
            f.write(default_storage.open(filename).read())

        subprocess.check_call((
            'convert',
            '-density', '288', # supersampling
            src,
            '-resize', '940x', # span12
            '%s/%%d.png' % tempdir,
        ))

        for x in session.preview_images.all():
            x.delete()

        for idx, filename in enumerate(sorted(os.listdir(tempdir))):
            if not filename.endswith('.png'):
                continue
            image = session.preview_images.create(order=idx)
            image.image.save(File(open(os.path.join(tempdir, filename))))

    finally:
        shutil.rmtree(tempdir)

    session.generating_pdf = False
    session.save(update_fields=('generating_pdf',))

    return "%d page(s)" % session.preview_images.count()
