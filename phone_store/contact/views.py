from django.shortcuts import render


# Create your views here.
def contact(request):
    context = {}
    context['chapter'] = 'contact'
    return render(request, 'contact/contact.html', context)
