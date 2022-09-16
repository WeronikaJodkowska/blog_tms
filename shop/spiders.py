import logging

from decimal import Decimal

import requests
import scrapy
from django.conf import settings

logger = logging.getLogger(__name__)


class OmaSpider(scrapy.Spider):
    name = "oma.by"
    start_urls = ["https://www.oma.by/elektroinstrument-c"]

    def parse(self, response, **kwargs):
        for product in response.css(".catalog-grid .product-item"):
            try:
                cost = product.css(".product-price-block .price__normal::text").get().strip()
                cost = Decimal(cost.replace(",", "."))
            except Exception:
                cost = 0

            file_name = None
            image_url = product.css(".product-item_img-box .catlg_list_img::attr(data-src)").get()
            if image_url:
                r = requests.get(f"https://www.oma.by/{image_url}", allow_redirects=True)
                if r.status_code == 200:
                    file_name = image_url.split("/")[-1]
                    open(settings.MEDIA_ROOT / file_name, "wb").write(r.content)

            data = {
                "external_id": product.attrib.get("data-ga-product-id"),
                "title": product.css(".product-title-and-rate-block .wrapper::text").get().strip(),
                "cost": cost,
                "link": f"https://www.oma.by{product.css('a.area-link::attr(href)').get()}",
                "image": file_name
            }
            yield data

        next_page = response.css(".page-nav_box .btn__nav-right::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)