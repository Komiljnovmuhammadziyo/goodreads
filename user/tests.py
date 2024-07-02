from django.contrib.auth import get_user
from .models import CustomUser
from django.test import TestCase
from django.urls import reverse

class TestRegistration(TestCase):
    def test_user_registration(self):
        self.client.post(
            reverse('user:register_page'),

            data = {
                'username':'Muhammadziyo0568',
                'first_name':'Muhammadziyo',
                'last_name':'Komiljanov',
                'email':'muhammadziyo056@gmail.com',
                'password':'somepassword'
            }
        )
        user = CustomUser.objects.get(username='Muhammadziyo0568')
        self.assertEqual(user.first_name, 'Muhammadziyo')
        self.assertEqual(user.last_name, 'Komiljanov')
        self.assertEqual(user.email, 'muhammadziyo056@gmail.com')
        self.assertEqual(user.password, 'somepassword')

    def test_required_fields(self):
        response = self.client.post(
            reverse('user:register_page'),
            data={
                'first_name':'Muhammadziyo',
                'password':'somepassword'
            }
        )
        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 0)
        self.assertFormError(response, 'form','username','This field is required.')

    def test_invalid_email(self):
        response = self.client.post(
            reverse('user:register_page'),
            data={
                'username':'Muhammadziyo0265'
            }
        )

    def test_invalid_password(self):
        response = self.client.post(
            reverse('user:register_page'),
            data={
                'username':'Muhammadziyo0265',
                'email':'Muhammadziyo0265@gamil.com',
            }
        )
        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 0)
        self.assertFormError(response, 'form','password','Invalid Password.')

class LoginTest(TestCase):
    def test_success_login(self):
        db_user = CustomUser.objects.create(username='Muhammadziyo056', first_name='Muhammadziyo')
        db_user.set_password('somepassword')
        db_user.save()

        self.client.post(
            reverse('user:login_page'),
            data = {
                'username':'Muhammadziyo056',
                'password':'somepassword'
            }
        )

        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)
