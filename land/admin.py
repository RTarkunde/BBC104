from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Testimonials
from .models import CompanyInfo
from .models import Lead

class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_no', 'email_id', 'send_to_salesforce')
    list_display_links = ('name', )
    search_fields = ('name', 'contact_no' 'email', 'send_to_salesforce')
    list_per_page = 25

admin.site.register(Testimonials)
admin.site.register(Lead, LeadAdmin)
admin.site.register(CompanyInfo)
