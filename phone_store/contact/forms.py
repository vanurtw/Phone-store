from django import forms


class OfferForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your name*'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email address*'}))
    phone = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Your Phone'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message*'}))
