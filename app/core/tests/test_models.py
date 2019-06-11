from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import BaseUserManager


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@londonappdev.com'
        password = 'Testpass6697'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_nomalized(self):
        """Test the email for a new user is normalized"""
        email = 'F1.mika@Gmail.COM'
        user = get_user_model().objects.create_user(email, 'Test6679')

        self.assertEqual(user.email, BaseUserManager.normalize_email(email))

    def test_new_user_without_email(self):
        """Test creating a new user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'Test6677')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'melong1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
