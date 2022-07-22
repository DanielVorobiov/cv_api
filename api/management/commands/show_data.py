from django.core.management.base import BaseCommand

from common.cv_data import cv_data


class Command(BaseCommand):
    """
    Django command that prints the CV data to the console
    """
    help = 'Print requested category info from the CV'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **kwargs):
        category = kwargs['category'].lower()
        data = cv_data.get(category, f'There is no such category: {category}')
        self.stdout.write(data)
