from django.urls import path

import user
from user.views import UserCreateViews, LoginUserView

app_name = 'user'

urlpatterns = [
    path('register/', UserCreateViews.as_view(), name='register_page'),
    path('login/', LoginUserView.as_view(), name='login_page')
]