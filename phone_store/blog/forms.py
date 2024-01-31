from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Comment'}))

    class Meta:
        model = Comment
        fields = ['content']
