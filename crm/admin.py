from django.contrib import admin

from .models import Client, Employee, Application

admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Application)