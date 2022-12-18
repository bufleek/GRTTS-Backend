
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import User


class UserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user("1010", "test@mail.com", "a_strong_pass")

    def test_authentication(self):
        data = {
            'employee_id': self.user.username,
        }
        response = self.client.post('/api/auth/', data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.user.id)
