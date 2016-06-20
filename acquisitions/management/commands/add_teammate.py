#!/usr/bin/env python3
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
import pdb

class Command(BaseCommand):
    help = 'Add teammate'

    def add_arguments(self, parser):
        parser.add_argument('username', nargs='+', type=str)


    def handle(self, *args, **options):
        for username in options['username']:
            try:
                user = User.objects.get(username=username)
                user.is_staff = True
                user.is_superuser = True
                print('Making %s a superuser!' % username)
                user.save()

            except User.DoesNotExist:
                print("%s does not exist" % username)
