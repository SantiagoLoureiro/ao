from django.core.management.base import BaseCommand
from core.services import migrate

from apps.articles.models import ArticleWp
from core.models import RealtionIdSourceDestination
from utils.services import clean_destination_and_default_tables


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **kwargs):
        clean_destination_and_default_tables()
        migrate()
