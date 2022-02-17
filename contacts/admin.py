from django.contrib import admin
from .models import Contact
from .models import SalaryContact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'email_id', 'contact_no', 'create_date')
    list_display_links = ('id', 'name' )
    search_fields = ('name',  'email_id', 'contact_no')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)


class SalaryContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'email_id', 'contact_no', 'create_date')
    list_display_links = ('id', 'name' )
    search_fields = ('name',  'email_id', 'contact_no')
    list_per_page = 25

admin.site.register(SalaryContact, SalaryContactAdmin)
