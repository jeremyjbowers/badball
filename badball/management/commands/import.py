import csv
import ujson as json
import os

from dateutil.parser import parse
from django.apps import apps
from django.db import connection
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from nameparser import HumanName

from badball import models


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with open('data/2020/steamer_hit.csv', 'r') as readfile:
            for p in [dict(p) for p in csv.DictReader(readfile)]:
                name = HumanName(p['Name'])
                obj, created = models.Player.objects.get_or_create(name=p['Name'], first_name=name.first, last_name=name.last, fg_id=p['playerid'], position="OF/IF")
                if created:
                    print("++ %s" % obj)
                else:
                    print(obj)