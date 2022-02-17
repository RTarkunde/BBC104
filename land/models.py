from django.db import models
from datetime import datetime

# Create your models here.
class Testimonials(models.Model):
    testimonial = models.TextField(max_length=200)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.testimonial


class Lead(models.Model):
    name = models.TextField(max_length=200)
    current_organization = models.TextField(max_length=200)
    income_less_than_fifty_lakhs = models.BooleanField(default=False)
    salary_income      = models.IntegerField()
    rental_income      = models.IntegerField()
    interest_income    = models.IntegerField()
    capital_gains      = models.IntegerField()
    other_income       = models.IntegerField()
    email_id           = models.EmailField(max_length=100)
    contact_no         = models.TextField(max_length=12)
    marked_for_delete  = models.BooleanField(default=False)
    send_to_salesforce = models.BooleanField(default=False)
    sent_to_salesforce = models.BooleanField(default=False)
    send_to_csv        = models.BooleanField(default=False)
    sent_to_csv        = models.BooleanField(default=False)
    create_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email_id

class CompanyInfo(models.Model):
    first_name  = models.CharField(max_length=200)
    last_name    = models.CharField(max_length=200)
    company_address = models.CharField(max_length=200)
    company_logo = models.ImageField(upload_to='photos/%Y/%m/%d/')
