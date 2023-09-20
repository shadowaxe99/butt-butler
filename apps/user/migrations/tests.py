
import pytest
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='testuser', password='testpass123')

    def test_username_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEqual(field_label, 'username')

    def test_password_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('password').verbose_name
        self.assertEqual(field_label, 'password')

    def test_username_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEqual(max_length, 150)

    def test_object_name_is_username(self):
        user = User.objects.get(id=1)
        expected_object_name = f'{user.username}'
        self.assertEqual(expected_object_name, str(user))

@pytest.mark.django_db
def test_new_user():
    User.objects.create_user('test', 'test@test.com', 'testpass')
    assert User.objects.count() == 1
