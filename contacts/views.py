from django.shortcuts import render
from .models import SalaryContact
from .models import Contact
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages

from django.http import HttpResponse
# Include the `fusioncharts.py` file that contains functions to embed the charts.

# Create your views here.
# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        name           = request.POST['name']
        email_id       = request.POST['email_id']
        contact_no     = request.POST['contact_no']
        preferred_time = request.POST['preferred_time']
        country        = request.POST['country']
        zip_code       = request.POST['zip_code']

        has_contacted = Contact.objects.all().filter(contact_no=contact_no)
        if has_contacted:
                messages.error(request, 'You have already made an inquiry. Please wait until we get back to you.')
                return render(request, 'pages/home.html')

        contact = Contact(name=name, email_id=email_id,
                    contact_no=contact_no, preferred_time=preferred_time, country=country,
                    zip_code=zip_code, marked_for_delete  = False, send_to_salesforce = False,
                    sent_to_salesforce = False, send_to_csv = False,
                    sent_to_csv        = False
        )
#        salaryContact = SalaryContact(name=name,
#                salary_income=salary_income, rental_income=rental_income,
#                interest_income=interest_income, capital_gains=capital_gains,
##                current_organization = current_organization,
#                marked_for_delete  = False, send_to_salesforce = False,
#                sent_to_salesforce = False, send_to_csv        = False,
#                sent_to_csv        = False
#                )

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                'New 104pc Tax Inquiry',
                'You have a new inquiry. Please login to your admin panel for more info.',
                'rtarkund@gmail.com',
                [admin_email],
                fail_silently=False,
            )
#        salaryContact.save()
        contact.save()
        messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
#        return redirect('/home/')
        return render(request, 'pages/home.html')



#        income_less_than_fifty_lakhs = request.POST['income_less_than_fifty_lakhs']
#        salary_income      = request.POST['salary_income']
#        rental_income      = request.POST['rental_income']
#        interest_income    = request.POST['interest_income']
#        capital_gains      = request.POST['capital_gains']
#        other_income       = request.POST['other_income']
#        current_organization = request.POST['current_organization']
