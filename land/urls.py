"""bbc104 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url
from . import views
import contacts.views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('calculator', views.calculator, name='calculator'),
    path('yourname', views.get_name, name='get_name'),
    path('submit',views.submit, name='submit'),
    path('contact', contacts.views.inquiry, name='contact'),
    url(r'^submit_url', views.submit, name='submit'),
    #path('submit_url', views.submit, name='submit'),

#    path('<int:question_id>/', views.detail, name='detail'),
]
