import csv
import sys
from django.core.management.base import BaseCommand
from characters.models import Character

class Command(BaseCommand):
    help = "Loads characters from a csv"
    args = "<filename>"

    def handle(self, *args, **kwargs):
        filename, = args
        if filename == '-':
            f = sys.stdin
        else:
            f = open(filename, 'r')
        reader = csv.reader(f)
        for name, in reader:
            Character.objects.get_or_create(name=name)
            sys.stdout.write('.')
        sys.stdout.write('\r\n')
        f.close()
