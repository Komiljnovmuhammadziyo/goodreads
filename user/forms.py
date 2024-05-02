from django import forms
from django.contrib.auth.models import User


# class RegisterForm(forms.Form):
#     username = forms.CharField(max_length=120)
#     first_name = forms.CharField(max_length=120)
#     last_name = forms.CharField(max_length=120)
#     email = forms.EmailField()
#     password = forms.CharField(max_length=150)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
