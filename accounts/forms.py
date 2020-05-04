from django import forms


class UserLoginForm(forms.Form):
    """Form to be used to login users in"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
