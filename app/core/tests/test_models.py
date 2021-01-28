from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = "test@test.com"
        password = "password123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'amitbisht@GMAIL.com'
        user = get_user_model().objects.create_user(
            email,
            'test1235'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test2234')

    def test_create_new_super_user(self):
        user = get_user_model().objects.create_superuser(
            'amit@gmail.com',
            'test1234'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
