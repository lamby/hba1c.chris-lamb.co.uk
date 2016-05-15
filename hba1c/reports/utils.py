from reportlab.lib import utils
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import landscape, A4

from django.contrib.staticfiles.storage import staticfiles_storage

PAGE_SIZE = landscape(A4)

def render_pdf(session, fileobj):
    c = canvas.Canvas(fileobj, pagesize=PAGE_SIZE)

    # Header
    drawImage(c, 'image002.png', 1, 1.3, 2) # Litchdon
    drawImage(c, 'image020.png', 10, 1.3, 8) # Your sugar counts
    drawImage(c, 'image037.png', 22, 1.5, 6) # NHS Trust


    drawImage(c, 'image013.png', 2, 4.5, 11) # "One in 100"
    drawImage(c, 'image010.png', 2, 7.3, 11) # "One in 10"
    drawImage(c, 'image009.png', 5.4, 8.5, 11) # "above this level"

    drawImage(c, 'image005.png', 14, 4.5, 11) # background
    drawImage(c, 'image016.png', 25, 4.5, 1.8) # 100
    drawImage(c, 'image017.png', 25, 7.3, 1.5) # 58
    drawImage(c, 'image018.png', 25, 8.5, 1.5) # 48

    for idx, result in enumerate(session.results.all()[:4]):
        drawString(c, 24, 5, "%s" % result.value)

    drawImage(c, 'image041.png', 24, 5.5, 2) # arrow
    drawImage(c, 'image036.png', 20, 10, 5.5) # latest result

    drawImage(c, 'image014.png', 2, 10, 10) # what is

    drawImage(c, 'image011.png', 1, 12, 27.5) # Reducing..
    drawImage(c, 'image012.png', 1, 14, 10) # You can reduce
    drawImage(c, 'image025.png', 12, 14, 16.5) # Discuss

    c.showPage()
    c.save()

def drawString(canvas, x, y, *args, **kwargs):
    canvas.drawString(
        (x * cm),
        PAGE_SIZE[1] - (y * cm),
        *args,
        **kwargs
    )

def drawImage(canvas, filename, x, y, width, height=None):
    path = staticfiles_storage.path('images/f_reports_pdf/%s' % filename)

    if height is None:
        iw, ih = utils.ImageReader(path).getSize()
        aspect = ih / float(iw)
        height = width * aspect

    canvas.drawImage(
        path,
        x * cm,
        PAGE_SIZE[1] - (y * cm) - (height * cm),
        width=width * cm,
        height=height * cm,
        mask='auto'
    )
