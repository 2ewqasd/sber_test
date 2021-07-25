from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Client, Application, Employee


from rest_framework.test import force_authenticate


class ClientTest(TestCase):

    def setUp(self):

        self.user1 = get_user_model().objects.create_user(
            username='testuser',
            password='secret',
        )

        self.clients = Client.objects.create(
            user=self.user1,
            unic_name=1,
            first_name='1',
            second_name='1',
            middle_name='1',
            email='test@email.com',
        )

        self.user2 = get_user_model().objects.create_user(
                username='testuser2',
                email='test2@email.com',
                password='secret',
            )
           
        self.employee = Employee.objects.create(
            user=self.user2,
            unic_name=1,
            first_name='2',
            middle_name='2',
            second_name='2',
            speciality='master'
        )
      
        self.application = Application.objects.create(
            number=1,
            client=self.clients,
            employee=self.employee,
            apl_type='repair',
            status='open',
            start_date='2021-07-25',
            end_date='2021-07-29'
        )

        self.application = Application.objects.create(
            number=2,
            client=self.clients,
            employee=self.employee,
            apl_type='service',
            status='in_work',
            start_date='2021-07-25',
            end_date='2021-07-31'
        )

        self.application = Application.objects.create(
            number=3,
            client=self.clients,
            employee=self.employee,
            apl_type='consultation',
            status='closed',
            start_date='2021-07-25',
            end_date='2021-07-26'
        )

    def test_get_conten_without_token(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 401)

    def test_get_token(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='testuser')
        request = factory.get('')
        force_authenticate(request, user=user, token=user.auth_token)
        
    
        