from rest_framework import serializers

from .models import Client
from .models import Employee
from .models import Application


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['unic_name', 'first_name', 'middle_name', 'second_name', 'email', 'tg_nick']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['unic_name', 'first_name', 'middle_name', 'second_name', 'speciality', 'email', 'tg_nick']

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['number','client','employee','apl_type','status','start_date','end_date']