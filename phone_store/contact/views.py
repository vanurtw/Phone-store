from django.shortcuts import render
from .forms import OfferForm

# Create your views here.
def contact(request):
    context = {}
    form = OfferForm()
    context['form'] = form
    context['chapter'] = 'contact'
    return render(request, 'contact/contact.html', context)
