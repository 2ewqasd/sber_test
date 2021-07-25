from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


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

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unic_name = models.IntegerField(unique=True)
    first_name = models.TextField(max_length=20)
    second_name = models.TextField(max_length=50)
    middle_name = models.TextField(max_length=20)
    email = models.EmailField()
    tg_nick = models.TextField(null=True, blank=True)  # Optional

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.second_name}'


class Employee(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unic_name = models.IntegerField(unique=True)
    first_name = models.TextField(max_length=20)
    second_name = models.TextField(max_length=50)
    middle_name = models.TextField(max_length=20)
    speciality = models.CharField(choices=SPEC, max_length=13)
    email = models.EmailField()
    tg_nick = models.TextField(null=True, blank=True)  # Optional

    def __str__(self):
        return f'{self.second_name}: {self.speciality}'


class Application(models.Model):

    number = models.IntegerField(unique=True)
    client = models.ForeignKey(Client, on_delete=models.deletion.CASCADE)
    employee = models.ForeignKey(
        Employee,
        on_delete=models.deletion.CASCADE,
        null=True,
        blank=True
    )
    apl_type = models.CharField(choices=TYPE, max_length=12)
    status = models.CharField(choices=STATUS, max_length=7)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(help_text="Deadline")

    def __str__(self):
        return str(self.number)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    'for new users auto create token'
    if created:
        Token.objects.create(user=instance)
