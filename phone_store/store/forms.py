from django import forms
from .models import Comments


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea())

    # rating = forms.CharField()
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.base_fields['rating'].widget.attrs['class'] = 'form-rating'

    class Meta:
        model = Comments
        fields = ['rating', 'comment']


class SetQuantityGoods(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    count = forms.IntegerField(min_value=0)
