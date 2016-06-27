from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from django.db.models import fields, F


class Command(BaseCommand):
    help = "track Kanban card progress in KanbanHistory table"

    def add_arguments(self, parser):
        parser.add_argument('app', nargs=1, type=str)
        parser.add_argument('model', nargs=1, type=str)
        parser.add_argument('history', nargs=1, type=str)

    def handle(self, *args, **options):
        h = apps.get_model(options['app'][0], options['history'][0])
        m = apps.get_model(options['app'][0], options['model'][0])
        items = m.objects.all()
        for i in items:
            entry, created = h.objects.get_or_create(
                name=i,
                status=i.award_status # TODO: add argument to set this
            )
            print(entry, created)
            if not created:
                entry.days = F('days') + 1
            entry.save()
