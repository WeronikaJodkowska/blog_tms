from django.db.models import Sum, F, QuerySet
from django_rq import job
from django.core.cache import cache

from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings

from shop.models import Product
from shop.spiders import OmaSpider

import logging

logger = logging.getLogger(__name__)


def get_sorted_product(queryset: QuerySet, order_by: str):
    if order_by == "cost":
        return queryset.order_by("cost")
    elif order_by == "-cost":
        return queryset.order_by("-cost")
    elif order_by == "sold":
        queryset = queryset.annotate(sold=Sum(F("cost") * F("purchases__count")))
        return queryset.order_by("sold")
    elif order_by == "popular":
        queryset = queryset.annotate(popular=Sum("purchases__count"))
        return queryset.order_by("popular")
    return queryset


@job
def run_oma_spider(dry_run):
    if dry_run:
        Product.objects.all().delete()

    def crawler_results(signal, sender, item, response, spider):
        Product.objects.update_or_create(external_id=item["external_id"], defaults=item)

    dispatcher.connect(crawler_results, signal=signals.item_scraped)

    process = CrawlerProcess(get_project_settings())
    process.crawl(OmaSpider)
    process.start()


@job
def cost_out_of_stock(request):
    # logger.info("run_products_update is called")
    cost = request.GET.get("cost")

    if cost == 0:
        Product.objects.filter(cost=0).update(some_date_field="Out of Stock")

