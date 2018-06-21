from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import View, FormView, CreateView, DetailView
from .forms import ContactForm
from .models import Contact
# home views.
class HomeView(SuccessMessageMixin, CreateView):
  template_name = "pages/index.html"
  form_class = ContactForm
  success_url = '/'
  def get_context_data(self, *args, **kwargs):
      context = super(HomeView, self).get_context_data(*args, **kwargs)
      context['object'] = Contact.objects.filter().first()
      return context

  def get_success_message(self, cleaned_data):
    print(cleaned_data)
    return "Thank You For Joining! We will answer you in 24h"

def get_contact(request):
  contacts = Contact.objects.all()
  return render(request, "pages/contacts.html", {"contacts": contacts})