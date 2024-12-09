from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from weasyprint import HTML
from .forms import InvoiceForm, PayslipForm

from invoices.forms import PayslipForm
from .models import Invoice
from .utils import generate_invoice_pdf, generate_next_invoice_number

def create_invoice(request):
    # Dummy data (replace with real data in production)
    invoice = Invoice.objects.create(
        # invoice_number="INV-001",
        invoice_number=generate_next_invoice_number(),
        recipient_name="John Doe",
        recipient_email="john.doe@example.com",
        description="Monthly service charge",
        amount=100.00,
        due_date="2024-12-31"
    )
    pdf_path = generate_invoice_pdf(invoice)
    with open(pdf_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{invoice.invoice_number}.pdf"'
    return response

def payslip_form_view(request):
    if request.method == "POST":
        form = PayslipForm(request.POST)
        if form.is_valid():
            # Collect form data to pass to the payslip template
            context = form.cleaned_data
            # Calculate gross pay, deductions, and net pay dynamically
            context["gross_pay"] = float(
                context["basic_salary"] + context["overtime"] + context["bonuses"] + context["other_allowances"]
            )
            context["total_deductions"] = float(
                context["tax"] + context["social_security"] + context["health_insurance"] + context["other_deductions"]
            )
            context["net_pay"] = float(context["gross_pay"] - context["total_deductions"])
            return render(request, "payslip_template.html", context)
    else:
        form = PayslipForm()

    return render(request, "payslip_form.html", {"form": form})

def invoice_form_view(request):
    if request.method == "POST":
        form = InvoiceForm(request.POST)
        print(request.POST)  # Debugging: Check the POST data
        if form.is_valid():
            invoice_data = {
                "invoice_number": form.cleaned_data["invoice_number"],
                "recipient_name": form.cleaned_data["recipient_name"],
                "description": form.cleaned_data["description"],
                "amount": form.cleaned_data["amount"],
                "due_date": form.cleaned_data["due_date"].strftime("%Y-%m-%d"),
                "issued_date": datetime.now().strftime("%Y-%m-%d"),
            }

            if "generate_pdf" in request.POST:
                # Generate and return PDF
                html_string = render(
                    request, "invoice_template.html", {"invoice": invoice_data}
                ).content.decode("utf-8")
                response = HttpResponse(content_type="application/pdf")
                response["Content-Disposition"] = 'inline; filename="invoice.pdf"'
                HTML(string=html_string).write_pdf(response)
                return response

            # Otherwise, render the invoice
            return render(request, "invoice_template.html", {"invoice": invoice_data})
        else:
            print(form.errors)  # Debugging: Print form validation errors

    else:
        form = InvoiceForm()

    return render(request, "invoice_form.html", {"form": form})