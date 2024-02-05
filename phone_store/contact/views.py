from django.shortcuts import render
from .forms import OfferForm
from django.views.generic import FormView, TemplateView


# Create your views here.

class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = OfferForm
    extra_context = {'chapter': 'contact'}
    success_url = 'thanks'

    def form_valid(self, form):
        form.offer_send_mail()
        return super(ContactView, self).form_valid(form)


class ThanksView(TemplateView):
    template_name = 'contact/thanks.html'
    extra_context = {'chapter': 'contact'}
