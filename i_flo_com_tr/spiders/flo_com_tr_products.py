import scrapy
from scrapy.crawler import CrawlerProcess
import json
import re

from iv_flo_com_tr.i_flo_com_tr.spiders.locators import Locators
from iv_flo_com_tr.i_flo_com_tr.items import FloComTrItem


class FloComTrSpider(scrapy.Spider):
    name = 'flo_com_tr'
    start_urls = ['https://songtea.com/pages/tea-by-type']

    custom_settings = {
        'FEED_EXPORT_BATCH_ITEM_COUNT': 100,
        'FEED_FORMAT': 'csv',
        'FEED_URI': f"../../iii_results/%(batch_id)02d-{'_'.join(re.findall(r'[A-Z][^A-Z]*', __qualname__)[:-1]).lower()}.csv",
        'FEED_EXPORT_FIELDS': []
    }

    def parse(self, response, **kwargs):
        items = FloComTrItem()
        yield items


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(FloComTrSpider)
    process.start()
