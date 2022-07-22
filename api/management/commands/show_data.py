from django.core.management.base import BaseCommand

from common.cv_data import cv_data


class Command(BaseCommand):
    help = 'Print requested info from CV'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **kwargs):
        category = kwargs['category']
        data = cv_data.get(category, f'There is no such category: {category}')
        self.stdout.write(data)
