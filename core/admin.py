import django.contrib.auth.admin
from django.contrib import admin
from .models import *


@admin.register(Account)
class UserAdmin(django.contrib.auth.admin.UserAdmin):
    pass
