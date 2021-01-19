from django import forms


class LoginForm(forms.Form):
    # create a form that will be used to authenticate users against the database
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
