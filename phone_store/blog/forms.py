from django import forms
from .models import Categories


class CategorySetPostForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    category = forms.ModelChoiceField(queryset=Categories.objects.all(), label='Категория')
