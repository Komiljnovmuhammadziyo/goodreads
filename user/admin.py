from django.contrib import admin

from .models import CustomUser, Follow


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name')


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user_from', 'user_to', 'created')


