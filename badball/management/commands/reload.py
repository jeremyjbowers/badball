import os
from io import StringIO
os.environ['DJANGO_COLORS'] = 'nocolor'

from django.apps import apps
from django.db import connection
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from badball import models


class Command(BaseCommand):

    def handle(self, *args, **options):
        os.system('dropdb badball')
        os.system('createdb badball')
        call_command('migrate')
        call_command('loaddata', 'data/fixtures/badball.json')