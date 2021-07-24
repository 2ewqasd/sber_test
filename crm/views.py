from django.db.models import query
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework import filters
import datetime

from .models import Client, Employee, Application
from .serializers import ClientSerializer, EmployeeSerializer, ApplicationSerializer

class СlientViewSet(viewsets.ModelViewSet):
    
    serializer_class = ClientSerializer
    
    def get_queryset(self):
        queryset = Client.objects.all()
        username = self.request.query_params.get('unic_name')
        name = self.request.query_params.get('first_name')
        otch = self.request.query_params.get('middle_name')
        fam = self.request.query_params.get('second_name')
        emaill = self.request.query_params.get('email')
        tg = self.request.query_params.get('tg_nick')

        if username is not None:
            queryset = queryset.filter(unic_name=username)
        if name is not None:
            queryset = queryset.filter(first_name=name)
        if otch is not None:
            queryset = queryset.filter(middle_name=otch)
        if fam is not None:
            queryset = queryset.filter(second_name=fam)
        if emaill is not None:
            queryset = queryset.filter(email=emaill)    
        if tg is not None:
            queryset = queryset.filter(tg_nick=tg)    
        return queryset
        
    

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()
        username = self.request.query_params.get('unic_name')
        name = self.request.query_params.get('first_name')
        otch = self.request.query_params.get('middle_name')
        fam = self.request.query_params.get('second_name')
        spec = self.request.query_params.get('speciality')
        emaill = self.request.query_params.get('email')
        tg = self.request.query_params.get('tg_nick')

        if username is not None:
            queryset = queryset.filter(unic_name=username)
        if name is not None:
            queryset = queryset.filter(first_name=name)
        if otch is not None:
            queryset = queryset.filter(middle_name=otch)
        if fam is not None:
            queryset = queryset.filter(second_name=fam)
        if emaill is not None:
            queryset = queryset.filter(email=emaill)
        if spec:
            queryset = queryset.filter(speciality=spec)    
        if tg is not None:
            queryset = queryset.filter(tg_nick=tg)    
        return queryset

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        queryset = Application.objects.all()
        date_start = self.request.query_params.get('start_date')
        date_end = self.request.query_params.get('end_date')
        type_of_ap = self.request.query_params.get('apl_type')
        status_of_ap = self.request.query_params.get('status')
        client = self.request.query_params.get('client')
        employee = self.request.query_params.get('employee')

        if date_end:
            queryset = queryset.filter(end_date=date_end)
        if date_start:
            queryset = queryset.filter(start_date=date_start)
        if type_of_ap:
            queryset = queryset.filter(apl_type=type_of_ap)
        if status_of_ap:
            queryset = queryset.filter(status=status_of_ap)
        if client:
            queryset = queryset.filter(client=client)
        if employee:
            queryset = queryset.filter(employee=employee)
       
        
        return queryset

