import csv
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = csv.reader(file, delimiter=';')
            next(phones)
            for phone in phones:
                new_phone = Phone(
                    name=phone[1],
                    image=phone[2],
                    price=int(phone[3]),
                    release_date=phone[4],
                    lte_exists=bool(phone[5]))
                new_phone.get_slug()
                new_phone.save()
