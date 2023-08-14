from django.http import HttpResponse
from django.shortcuts import render
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.template import Context


def homePage(request):
    return render(request,"index.html")


def certificateUs(request):
    return render(request, "certificate.html")

def signIn(request):
    return render(request, "sign.html")

# def form_to_pdf(request):
#     # Handle form submission and process the form data if needed
#     # For simplicity, this example just renders the form template.
#     return render(request, 'certificate.html')

def form_to_pdf(request):
    # Your form processing logic goes here (if needed)

    # Get the HTML content of the form template
    template = get_template('certificate.html')
    context = {'csrf_token': request.COOKIES['csrftoken']}  # Pass the CSRF token to the template
    html = template.render(context)

    # Create a PDF from the HTML content
    result = BytesIO()
    # pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)

    # Check if the PDF generation was successful
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="form.pdf"'
        return response

    return HttpResponse("Error generating PDF", status=500)