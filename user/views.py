from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from user.forms import RegisterForm, LoginForm


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
            return redirect('users:login' )



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
        login_form = LoginForm

        context = {
            'form': login_form
        }

        return render(request, template_name='registration/login.html', context=context)
    def post(self, request):

        create_form = RegisterForm(data= request.POST)
        if create_form.is_valid():

            create_form.save()
            return redirect('users:login' )
