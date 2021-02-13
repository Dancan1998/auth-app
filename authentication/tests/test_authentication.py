from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()


class BaseTest(TestCase):
    def setUp(self):
        self.registerUrl = reverse('authentication:register')
        self.loginUrl = reverse('authentication:login')
        self.user = {
            'email': 'bob@example.com',
            'first_name': 'Bob',
            'last_name': 'Smith',
            'county': 'Kepler',
            'id_no': '12',
            'password': 'password123'
        }
        self.empy_email_cannot_register = {
            'email': ''
        }


class RegisterTest(BaseTest):
    def test_user_can_register(self):
        response = self.client.post(self.registerUrl, self.user)
        self.assertEqual(response.status_code, 201)

    def test_user_cannot_register_empty_email(self):
        response = self.client.post(
            self.registerUrl, self.empy_email_cannot_register)
        self.assertEqual(response.status_code, 400)


class LoginTest(BaseTest):
    def test_user_can_login(self):
        self.client.post(self.registerUrl, self.user)
        user = User.objects.filter(email=self.user.get('email')).first()
        user.save()
        response = self.client.post(self.loginUrl, self.user)
        self.assertEqual(response.status_code, 200)
