from django.template.loader import render_to_string
from invoices.models import Invoice
from weasyprint import HTML
import uuid
import os

def generate_invoice_pdf(invoice):
    context = {
        'invoice': invoice
    }
    html_string = render_to_string('invoice_template.html', context)
    html = HTML(string=html_string)
    output_path = f"invoices/{invoice.invoice_number}.pdf"
    html.write_pdf(target=output_path)
    return output_path


def generate_next_invoice_number():
    """
    Generate a unique invoice number using UUID.
    """
    unique_id = uuid.uuid4().hex[:8]  # Get a shortened 8-character unique string
    return f"INV-{unique_id}"


# def generate_next_invoice_number():
#     """
#     Helper function to generate the next invoice number.
#     It checks the latest invoice number and increments it.
#     """
#     last_invoice = Invoice.objects.order_by('-issued_date').first()
#     if last_invoice and last_invoice.invoice_number:
#         # Extract the numeric part and increment
#         last_number = int(last_invoice.invoice_number.split('-')[-1])
#         new_number = last_number + 3
#     else:
#         # No previous invoices exist
#         new_number = 1
#     return f"INV-{new_number:03d}"  # Format with leading zeros like 'INV-001'


