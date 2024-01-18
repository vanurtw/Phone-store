from django import forms
from .models import Comments


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea())
    class Meta:
        model = Comments
        fields = ['rating', 'comment']
