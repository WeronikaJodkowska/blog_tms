from django.core.management.base import BaseCommand

from shop.services import run_oma_spider


class Command(BaseCommand):
    help = "Crawl OMA catalog"

    def add_arguments(self, parser):
        parser.add_argument("--dry_run", type=bool)

    def handle(self, *args, **options):
        dry_run = options.get("dry_run", False)
        run_oma_spider.delay(dry_run)
