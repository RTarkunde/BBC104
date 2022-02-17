from django.shortcuts import render, get_object_or_404
from .models import Testimonials
from .models import CompanyInfo
from django.contrib import messages
from .models import Lead
from django.http import HttpResponseRedirect, HttpResponse
from .forms import NameForm
import logging
# Create your views here.
#def home(request):
#    return render(request, 'pages/home.html')
def home(request):
    latest_testimonial_list = Testimonials.objects.order_by('-pub_date').filter(is_featured=True)[:3]
    company_info_list = CompanyInfo.objects.order_by('-first_name')
    context = {'latest_testimonial_list': latest_testimonial_list, 'company_info_list': company_info_list }
    logging.info(company_info_list)
    return render(request, 'pages/home.html', context)

def calculator(request):
    company_info_list = CompanyInfo.objects.order_by('-first_name')
    context = {'company_info_list': company_info_list }
    return render(request, 'pages/calculator.html', context)
#    return HttpResponse("You're looking at calculator.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def submit(request):
    if request.method == 'POST':
        name = request.POST['name']
        current_organization = request.POST['current_organization']
        income_less_than_fifty_lakhs = request.POST['income_less_than_fifty_lakhs']
        salary_income      = request.POST['salary_income']
        rental_income      = request.POST['rental_income']
        interest_income    = request.POST['interest_income']
        capital_gains      = request.POST['capital_gains']
        other_income       = request.POST['other_income']
        email_id           = request.POST['email_id']
        contact_no         = request.POST['contact_no']
        create_date = models.DateTimeField(blank=True, default=datetime.now)

    else:
        lead = Lead(name = name, current_organization = current_organization,
            income_less_than_fifty_lakhs = income_less_than_fifty_lakhs,
            salary_income      = salary_income,
            rental_income      = rental_income,
            interest_income    = interest_income,
            capital_gains      = capital_gains,
            other_income       = other_income,
            email_id           = email_id,
            contact_no         = contact_no,
            marked_for_delete  = FALSE,
            send_to_salesforce = FALSE,
            sent_to_salesforce = FALSE,
            send_to_csv        = FALSE,
            sent_to_csv        = FALSE,
            create_date = create_date)
        lead.save()
        # messages.success(request, 'Your request has been submiited')
        # return redirect('/cars/'+car_id)

        #return render(request, 'pages/submission.html')
        return redirect('pages/submission.html')

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'pages/name.html', {'form': form})


name">
<input class="w3-input w3-section w3-border" type="text" placeholder="Email" required name="email_id">
<input class="w3-input w3-section w3-border" type="text" placeholder="Contact" required name="contact_no">
<input class="w3-input w3-section w3-border" type="text" placeholder="Prefered Time " required name="preferred_time">
<input class="w3-input w3-section w3-border" type="text" placeholder="Country " required name="country">
<input class="w3-input w3-section w3-border" type="text" placeholder="ZIP code/Pin code" required name="zip_code">

def contact(request):
    if request.method == 'POST':
        name       = request.POST['name']
        email_id   = request.POST['email_id']
        subject    = request.POST['country']
        contact_no = request.POST['contact_no']
        zip_code   = request.POST['zip_code']
        preferred_time   = request.POST['preferred_time']


        ]

     return HttpResponse("You're looking at contact.")
