from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from user.forms import RegisterForm


class UserCreateViews(View):
    def get(self,request):

        register_form = RegisterForm

        context = {
            'form':register_form
        }

        return render(request, template_name='register.html', context=context)
    def post(self, request):

        create_form = RegisterForm(data= request.POST)
        if create_form.is_valid():

            create_form.save()
            return redirect('user:login_page' )



        # username = request.POST['username']
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # email = request.POST['email']
        # password = request.POST['password']
        #
        # user = User.objects.create_user(username=username,
        #                          first_name=first_name,
        #                          last_name=last_name,
        #                          email=email,
        #                          password=password
        # )
        # user.save()
        #
        # print(username, first_name, last_name, email, password)

        # return render(request, template_name='login.html')
        else:
            context = {
                'form':create_form
            }
            return render(request, template_name='register.html', context=context)

class LoginUserView(View):
    def get(self, request):
        login_form = AuthenticationForm
        user = request.user
        user_se_key = request.COOKIES.get('sessionid')
        print(user.is_authrnticated)
        print(user_se_key)
        context = {
            'form': login_form
        }

        return render(request, template_name='registration/login.html', context=context)
    def post(self, request):

        login_form = AuthenticationForm(data= request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)

            return redirect('landing_page.html')

        else:
            return render(request, template_name='registration/login.html', context={'form':login_form})
