from django.test import TestCase
from ..models import User


class UserModelTestCase(TestCase):
    def test_valid_create_user(self):
        User.objects.create_user(username="TestVlad", email="testEmail@gmail.com", password="TestPassword123")
        users_count = len(User.objects.all())
        expected_count = 1
        self.assertEqual(expected_count, users_count)

    def test_valid_delete_user(self):
        User.objects.create_user(username="TestVlad", email="testEmail@gmail.com", password="TestPassword123")
        user1 = User.objects.get(username="TestVlad")
        user1.delete()
        users_count = 0
        expected_count = 0

        self.assertEqual(expected_count, users_count)

    def test_valid_update_user(self):
        User.objects.create_user(username="TestVlad", email="testEmail@gmail.com", password="TestPassword123")
        user1 = User.objects.get(username="TestVlad")

        new_username = "TestVova"
        new_email = "testVovaEmail@gmail.com"
        new_password = "TestVovaPassword123"

        user1.username = new_username
        user1.email = new_email
        user1.password = new_password

        self.assertEqual(new_username, user1.username)
        self.assertEqual(new_email, user1.email)
        self.assertEqual(new_password, user1.password)
