from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            forms.ValidationError('Пароли не совпадают!')
        return cd['password']
