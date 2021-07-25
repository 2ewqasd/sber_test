from django.db.models import Q
from rest_framework import permissions
from rest_framework import viewsets


from .models import Client, Employee, Application
from .serializers import ClientSerializer, EmployeeSerializer, ApplicationSerializer

class СlientViewSet(viewsets.ModelViewSet):
    '''
    Typical filters and permission access
    '''
    
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAdminUser|permissions.IsAuthenticated]
    
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
    '''
    Typical filters and permission access
    '''

    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAdminUser|permissions.IsAuthenticated]

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

    '''
    Typical permission access and filters not include timeline
    TIMELINE:
    Choice what we will include
    fs,fe - filter_start,filter_end
    ds,de - date_start, date_end
    ('fs', 'ds', 'de', 'fe')
    date_start__gte, date_end__lte
    ('ds', 'fs', 'fe', 'de')
    date_start_lte, date_end__gt
    ('ds', 'fs', 'de', 'fe')
    date_end__range
    ('fs', 'ds', 'fe', 'de')
    date_start__range 
    '''
    
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAdminUser|permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Application.objects.all()
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        type_of_ap = self.request.query_params.get('apl_type')
        status_of_ap = self.request.query_params.get('status')
        client = self.request.query_params.get('client')
        employee = self.request.query_params.get('employee')

        if type_of_ap:
            queryset = queryset.filter(apl_type=type_of_ap)
        if status_of_ap:
            queryset = queryset.filter(status=status_of_ap)
        if client:
            queryset = queryset.filter(client=client)
        if employee:
            queryset = queryset.filter(employee=employee)
        if start_date and end_date:
            '''
            TIMELINE START HERE
            '''
            queryset = queryset.filter(
                Q(start_date__gte=start_date, end_date__lte=end_date) |
                Q(start_date__lte=start_date, end_date__gte=end_date) |
                Q(end_date__range=(start_date, end_date)) |
                Q(start_date__range=(start_date, end_date))
            )
        elif end_date:
            queryset = queryset.filter(end_date=end_date)
        elif start_date:
            queryset = queryset.filter(start_date=start_date)

    #    TODO: date_start < date_end
        
        return queryset

