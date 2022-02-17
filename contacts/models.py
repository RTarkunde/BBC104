from django.db import models
from datetime import datetime
# Create your models here.
class Contact(models.Model):
        name               = models.CharField(max_length=200)
        email_id           = models.EmailField(max_length=100)
        contact_no         = models.CharField(max_length=12)
        preferred_time      = models.CharField(max_length=100)
        country            = models.CharField(max_length=100)
        zip_code           = models.IntegerField()
        create_date        = models.DateTimeField(blank=True, default=datetime.now)
        marked_for_delete  = models.BooleanField(default=False)
        send_to_salesforce = models.BooleanField(default=False)
        sent_to_salesforce = models.BooleanField(default=False)
        send_to_csv        = models.BooleanField(default=False)
        sent_to_csv        = models.BooleanField(default=False)

class SalaryContact(models.Model):
        name               = models.CharField(max_length=200)
        email_id           = models.EmailField(max_length=100)
        contact_no         = models.CharField(max_length=12)
        current_organization= models.CharField(max_length=100)
        create_date        = models.DateTimeField(blank=True, default=datetime.now)
        salary_income      = models.IntegerField()
        rental_income      = models.IntegerField()
        interest_income    = models.IntegerField()
        capital_gains      = models.IntegerField()
        other_income       = models.IntegerField()
        marked_for_delete  = models.BooleanField(default=False)
        send_to_salesforce = models.BooleanField(default=False)
        sent_to_salesforce = models.BooleanField(default=False)
        send_to_csv        = models.BooleanField(default=False)
        sent_to_csv        = models.BooleanField(default=False)
