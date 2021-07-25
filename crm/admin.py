from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Client, Employee, Application

class ClientInline(admin.StackedInline):
    'Include client like user in admin'
    model = Client
    can_delete = False
    verbose_name_plural = 'client'

class EmployeeInline(admin.StackedInline):
    'Include employee like user in admin'
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

class UserAdmin(BaseUserAdmin):
    inlines = (ClientInline, EmployeeInline)

class ApplicationAdmin(admin.ModelAdmin):
    model = Application
    list_display = ['number', 'apl_type', 'status', 'start_date', 'end_date']

class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ['unic_name', 'first_name', 'middle_name', 'second_name']

class EmployeeAdmin(admin.ModelAdmin):
    model = Client
    list_display = ['unic_name', 'first_name', 'second_name', 'speciality']

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Application, ApplicationAdmin)