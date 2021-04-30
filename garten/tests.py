from django.test import TestCase, Client
from garten.models import *
from django.contrib.auth.models import User

class TestApplication(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()

    
    def test_sendApplication(self):
        login = self.client.login(username='testuser', password='12345')

        headers={'Content-Type' : 'application/x-www-form-urlencoded'}
        data= {
            'parent_first_name': 'testFirstName',
            'parent_last_name': 'testLastName',
            'income': 1000,
            'child_first_name': 'testFirstName',
            'child_last_name': 'testLastName',
            'age': 4
        }
        response = self.client.post('/apply',headers=headers,data=data)
        print(response)

