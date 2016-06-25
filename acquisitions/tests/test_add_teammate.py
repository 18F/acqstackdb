from django.core.management import call_command
from django.test import TestCase
from django.contrib.auth.models import User


class AddTeammateTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test_user', email='',
                                             password='')
        self.assertFalse(self.user.is_superuser, 'User *is not* an admin \
                                                  before the command.')

    def test_superuser_command_output(self):
        call_command('add_teammate', 'test_user')
        self.user = User.objects.get(username='test_user')
        self.assertTrue(self.user.is_superuser, 'User *is* an admin \
                                                 after the command.')
