from django.db import models
from django.db.models.deletion import CASCADE

SPEC = [
    ('consultant', 'Consultant'),
    ('master', 'Master'),
    ('service_staff', 'Service staff')
]

TYPE = [
    ('repair', 'Repair'),
    ('service', 'Service'),
    ('consultation', 'Consultation')
]

STATUS = [
    ('open', 'Open'),
    ('in_work', 'In work'),
    ('closed', 'Closed')
]

class Client(models.Model):

    unic_name = models.TextField(max_length=20, default=1)
    first_name = models.TextField(max_length=20)
    second_name = models.TextField(max_length=50)
    middle_name = models.TextField(max_length=20)
    email = models.EmailField()
    tg_nick = models.TextField(null=True, blank=True) #Optional

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.second_name}'

class Employee(models.Model):

    unic_name = models.TextField(max_length=20, default=1)
    first_name = models.TextField(max_length=20)
    second_name = models.TextField(max_length=50)
    middle_name = models.TextField(max_length=20)
    speciality = models.CharField(choices=SPEC, max_length=13)
    email = models.EmailField()
    tg_nick = models.TextField(null=True, blank=True) #Optional

    def __str__(self):
        return f'{self.second_name}: {self.speciality}'
    
class Application(models.Model):

    number = models.TextField(max_length=20)
    client = models.ForeignKey(Client, on_delete=CASCADE)
    employee = models.ForeignKey(Employee, on_delete=CASCADE, null=True, blank=True)
    apl_type = models.CharField(choices=TYPE, max_length=12)
    status = models.CharField(choices=STATUS, max_length=7)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(help_text="Deadline")

    def __str__(self):
        return self.number
