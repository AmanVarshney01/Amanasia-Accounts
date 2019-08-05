from django.db import models
from datetime import date

# Create your models here.
class Entries(models.Model):
    purchaser_name = models.CharField(max_length=30)
    purchaser_address = models.TextField()
    gstin_no = models.IntegerField()
    description = models.CharField(max_length=25)
    hsn_code = models.IntegerField()
    quantity = models.IntegerField()
    rate = models.IntegerField()
    taxable_value = models.IntegerField()
    packaging = models.IntegerField()
    total_amount_before_tax = models.IntegerField()
    cgst = models.IntegerField()
    sgst = models.IntegerField()
    total_amount_after_tax = models.IntegerField()
    date = models.DateField(("Date"), auto_now_add=True)
