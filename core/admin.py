import django.contrib.auth.admin
from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(django.contrib.auth.admin.UserAdmin):
    pass
