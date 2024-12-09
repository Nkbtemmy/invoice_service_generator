from django.db import models

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50, unique=True)
    recipient_name = models.CharField(max_length=255)
    recipient_email = models.EmailField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    issued_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Invoice {self.invoice_number}"
