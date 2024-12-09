from django.urls import path
from invoices import views

urlpatterns = [
    path('', views.create_invoice, name='generate_invoice'),
    path('payslip/form/', views.payslip_form_view, name="payslip_form"),
    path('generate-invoice/', views.invoice_form_view, name="generate_invoice_form"),
]
