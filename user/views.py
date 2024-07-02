from tokenize import Comment

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView

from book.forms import CommentForm
from .models import CustomUser, Follow
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from user.forms import RegisterForm, UpdateProfileForm


class UserCreateViews(View):
    def get(self,request):
        register_form = RegisterForm
        messages.info(request,'You have an account now you need login')
        context = {
            'form':register_form
        }

        return render(request, template_name='registration/register.html', context=context)
    def post(self, request):

        create_form = RegisterForm(data= request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('user:login_page' )
        else:
            context = {
                'form':create_form
            }
            return render(request, template_name='registration/register.html', context=context)

class LoginUserView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        # user = request.user
        # user_se_key = request.COOKIES.get('sessionid')
        # print(user.is_authenticated)
        # print(user_se_key)
        context = {
            'form': login_form
        }

        return render(request, template_name='registration/login.html', context=context)
    def post(self, request):

        login_form = AuthenticationForm(data= request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, 'You have been Log In now')
            return redirect('landing_page')

        else:
            return render(request, template_name='registration/login.html', context={'form':login_form})


class ProfileView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'registration/profile.html',{'user': request.user})



class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request,'You have been logged out')
        return redirect('landing_page')

class UpdateProfileView(LoginRequiredMixin, View):
    def get(self, request):
        userform = UpdateProfileForm(instance=request.user)

        return render(request, 'registration/profile_update.html', {'form': userform})

    def post(self, request):
        user = UpdateProfileForm(instance=request.user,
                                 data=request.POST,
                                 files=request.FILES
                                 )

        if user.is_valid():
            user.save()
            messages.success(request,'Your updates is save !')
            return redirect('user:profile')
        return render(request,'registration/profile_update.html', {'form':user})

class UserDetailView(View):
    user = CustomUser.objects.all()
    def get(self, request, user_id):
        user = CustomUser.objects.get(pk=user_id)
        follow_count = Follow.objects.all().count()
        context = {
            'user': user,
            'follow_count': follow_count
        }
        return render(request, 'registration/user_detail.html',context)
# @login_required
# def follow_user(request, user_id):
#     user_to_follow = get_object_or_404(CustomUser, id=user_id)
#     if request.user == user_to_follow:
#         return HttpResponseForbidden("You cannot follow yourself.")
#     request.user.follow(user_to_follow)
#     return redirect('user:user_detail', user_id=user_id)
#
# @login_required
# def unfollow_user(request, user_id):
#     user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
#     if request.user == user_to_unfollow:
#         return HttpResponseForbidden("You cannot unfollow yourself.")
#     request.user.unfollow(user_to_unfollow)
#     return redirect('user:user_detail', user_id=user_id)
#
# def user_profile(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     is_following = request.user.is_following(user) if request.user.is_authenticated else False
#     return render(request, 'registration/user_detail.html', {'user': user, 'is_following': is_following})


User = get_user_model()

@login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    if request.user == user_to_follow:
        return HttpResponseForbidden("You cannot follow yourself.")
    request.user.follow(user_to_follow)
    return redirect('user:user_detail', user_id=user_id)

@login_required
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    if request.user == user_to_unfollow:
        return HttpResponseForbidden("You cannot unfollow yourself.")
    request.user.unfollow(user_to_unfollow)
    return redirect('user:user_detail', user_id=user_id)

def user_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    is_following = request.user.is_following(user) if request.user.is_authenticated else False
    # is_following = True
    # print(is_following)
    return render(request, 'registration/user_detail.html', {'user': user, 'is_following': is_following})

class UserListView(View):

    def get(self, request):
        user = CustomUser.objects.all()
        context = {
            'user':user
        }
        search_query = request.GET.get('q')
        if search_query:
            users = user.filter(title__icontains=search_query)

            page_size = request.GET.get('page_size', 3)
            paginator = Paginator(users, page_size)

            page_num = request.GET.get('page', 1)
            page_obj = paginator.get_page(page_num)

            context = {"page_obj": page_obj}
            return render(request, 'registration/user_list.html', context)
        return render(request, 'registration/users_list.html', context)


