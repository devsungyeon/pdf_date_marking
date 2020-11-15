from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import datetime

def pdf_date_marking(filename):

    # Read your existing PDF
    existing_pdf = PdfFileReader(open(filename+'.pdf', "rb"))
    pagesnumber = existing_pdf.getNumPages()
    output = PdfFileWriter()

    day = datetime.date(2020,11,3)
    j = 1
    for i in range(pagesnumber):

        packet = io.BytesIO()
        # Create a new PDF with Reportlab
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFont('Helvetica-Bold', 12)

        if j == 3:
            day = day + datetime.timedelta(days=1)
            j = 1
        j = j + 1
        can.drawString(10, 700, str(day))
        can.showPage()
        can.save()
        # Move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)    

        # Add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(i)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

    day = datetime.date(2020,12,23)
    j = 1
    for i in range(pagesnumber):

        packet = io.BytesIO()
        # Create a new PDF with Reportlab
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFont('Helvetica-Bold', 12)

        if j == 3:
            day = day + datetime.timedelta(days=1)
            j = 1
        j = j + 1
        can.drawString(100, 700, str(day))
        can.showPage()
        can.save()
        # Move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)    

        # Add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(i)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)
        
        
    # Finally, write "output" to a real file
    outputStream = open(filename + '_done.pdf', "wb")
    output.write(outputStream)
    outputStream.close()