from django import forms
from django.core.mail import send_mail


class OfferForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your name*'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email address*'}))
    phone = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Your Phone'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message*'}))

    def offer_send_mail(self):
        subject = 'Offer'
        message = f"{self.cleaned_data['text']}\nphone: {self.cleaned_data['phone']}"
        send_mail(subject, message, 'vanuartw@mail.ru', [self.cleaned_data['email']])
