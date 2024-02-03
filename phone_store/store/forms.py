from django import forms
from .models import Comments, NewsletterSub


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.base_fields['rating'].widget.attrs['class'] = 'form-rating'

    class Meta:
        model = Comments
        fields = ['rating', 'comment']


class SetQuantityGoods(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    count = forms.IntegerField(min_value=0)


class NewsletterSubForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'email', 'placeholder': 'Enter your email address...'}))

    class Meta:
        model = NewsletterSub
        fields = ['email']
