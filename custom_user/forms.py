from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, max_length=20)


class CustomUserForm(forms.Form):
    username = forms.CharField(max_length=50)
    display_name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, max_length=20)
