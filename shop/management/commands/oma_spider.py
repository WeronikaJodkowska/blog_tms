import argparse

from django.core.management.base import BaseCommand
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings

from shop.models import Product
from shop.spiders import OmaSpider


class Command(BaseCommand):
    help = "Crawl OMA catalog"

    def add_arguments(self, parser):
        parser.add_argument("--dry_run", type=bool)

    def handle(self, *args, **options):
        dry_run = options.get("dry_run", False)
        if dry_run:
            Product.objects.all().delete()

        def crawler_results(signal, sender, item, response, spider):
            Product.objects.update_or_create(external_id=item["external_id"], defaults=item)
        dispatcher.connect(crawler_results, signal=signals.item_scraped)

        process = CrawlerProcess(get_project_settings())
        process.crawl(OmaSpider)
        process.start()