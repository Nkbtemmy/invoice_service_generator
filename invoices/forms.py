from django import forms


class PayslipForm(forms.Form):
    # Employee details
    employee_name = forms.CharField(max_length=255, label="Employee Name")
    employee_id = forms.CharField(max_length=255, label="Employee ID")
    department = forms.CharField(max_length=255, label="Department")
    position = forms.CharField(max_length=255, label="Position")

    # Pay period details
    payment_date = forms.DateField(label="Payment Date", widget=forms.DateInput(attrs={"type": "date"}))
    period_start = forms.DateField(label="Start Date", widget=forms.DateInput(attrs={"type": "date"}))
    period_end = forms.DateField(label="End Date", widget=forms.DateInput(attrs={"type": "date"}))

    # Earnings details
    basic_salary = forms.DecimalField(max_digits=10, decimal_places=2, label="Basic Salary")
    overtime = forms.DecimalField(max_digits=10, decimal_places=2, label="Overtime", initial=0)
    bonuses = forms.DecimalField(max_digits=10, decimal_places=2, label="Bonuses", initial=0)
    other_allowances = forms.DecimalField(max_digits=10, decimal_places=2, label="Other Allowances", initial=0)

    # Deductions
    tax = forms.DecimalField(max_digits=10, decimal_places=2, label="Tax", initial=0)
    social_security = forms.DecimalField(max_digits=10, decimal_places=2, label="Social Security", initial=0)
    health_insurance = forms.DecimalField(max_digits=10, decimal_places=2, label="Health Insurance", initial=0)
    other_deductions = forms.DecimalField(max_digits=10, decimal_places=2, label="Other Deductions", initial=0)

class InvoiceForm(forms.Form):
    invoice_number = forms.CharField(label="Invoice Number", max_length=50, required=True)
    recipient_name = forms.CharField(label="Recipient Name", max_length=100, required=True)
    description = forms.CharField(label="Description", widget=forms.Textarea(attrs={"rows": 2}), required=True)
    amount = forms.DecimalField(label="Amount", min_value=0, max_digits=10, decimal_places=2, required=True)
    due_date = forms.DateField(label="Due Date", widget=forms.DateInput(attrs={"type": "date"}), required=True)
