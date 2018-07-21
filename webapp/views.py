from django.shortcuts import render
from .models import ContactModel
from .forms import ContactForm
from django.views.generic import CreateView
# Create your views here.


class ContactView(CreateView):
	model = ContactModel
	form_class = ContactForm
	template_name = 'index.html'
	success_url = '/thankyou'

