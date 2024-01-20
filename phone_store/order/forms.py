from .models import Order
from django import forms


class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.base_fields['city'].label = 'Your city *'

    first_name = forms.CharField(label='First Name *', max_length=50,
                                 widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    last_name = forms.CharField(label='Last Name *', max_length=50,
                                widget=forms.TextInput(attrs={'placeholder': 'Your last name'}))
    company_name = forms.CharField(label='Company Name', max_length=80, required=False,
                                   widget=forms.TextInput(attrs={'placeholder': 'Your company name'}))
    address = forms.CharField(label='Street Address *',
                              widget=forms.TextInput(attrs={'placeholder': 'Street, house, flat'}))
    postcode = forms.CharField(max_length=20, label='Postcode / ZIP *',
                               widget=forms.TextInput(attrs={'placeholder': 'Your postal code'}))
    phone = forms.CharField(max_length=20, label='Phone *',
                            widget=forms.TextInput(attrs={'placeholder': 'Your phone number'}))
    email = forms.CharField(label='Email Address *', widget=forms.EmailInput(attrs={'placeholder': 'Your email'}))
    order_notes = forms.CharField(label='Order Notes', required=False,
                                  widget=forms.Textarea(attrs={'placeholder': 'Leave a comment on your order'}))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'company_name', 'address', 'city', 'postcode', 'phone', 'email',
                  'order_notes']
