from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_creat_user_email_succesful(self):
        email='hello.com'
        password='123123'
        user =get_user_model().objects.create_user(
        email=email,
        password=password

        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.check_password(password),True)
    def test_new_user_normalize(self):
        email="test@gmail.com"

        user =get_user_model().objects.create_user(
        email,'123123'
        )

        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')



    def test_creat_new_super_user(self):
        user=get_user_model().objects.create_superuser(
        'test@gmail.com',
        '123123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
