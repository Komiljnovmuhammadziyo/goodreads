from django import forms
from django.core.mail import send_mail

from user.models import CustomUser


# class RegisterForm(forms.Form):
#     username = forms.CharField(max_length=120)
#     first_name = forms.CharField(max_length=120)
#     last_name = forms.CharField(max_length=120)
#     email = forms.EmailField()
#     password = forms.CharField(max_length=150)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password','gender')

    def save(self, commit=True):

        user = super().save(commit)
        if self.cleaned_data['gender'] =='F':
            user.profile_picture = 'default_famale-picture_KeGFIrW.jpg'
        elif self.cleaned_data['gender'] == 'M':
            user.profile_picture ='default_pic.jpg'

        user.set_password(self.cleaned_data['password'])
        user.save()
        if user.email:
            send_mail(
                'Your Goodreads account has been created.',
                'Welcome to Goodreads clone!',
                'muhammadziyo056@gmail.com',
                [user.email],
            )
        return user

# class LoginForm(forms.ModelForm):
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(max_length=128)
#
#     def clean(self):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
#


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email','profile_picture')


