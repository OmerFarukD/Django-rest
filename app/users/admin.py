from django.contrib import admin

from .models import CustomUser
from rest_framework.authtoken.admin import TokenAdmin
# Register your models here.
TokenAdmin.raw_id_fields = ['user']

admin.site.register(CustomUser)