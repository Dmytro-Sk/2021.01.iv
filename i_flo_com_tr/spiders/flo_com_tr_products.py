import scrapy
from scrapy.crawler import CrawlerProcess
import json
import re

from iv_flo_com_tr.i_flo_com_tr.spiders.locators import Locators
from iv_flo_com_tr.i_flo_com_tr.items import FloComTrItem


class FloComTrSpider(scrapy.Spider):
    name = 'flo_com_tr'
    start_urls = ['https://www.flo.com.tr/tum-kategoriler']

    custom_settings = {
        'ITEM_PIPELINES': {
            'iv_flo_com_tr.i_flo_com_tr.pipelines.FloComTrPipeline': 300
        },
        'FEED_EXPORT_BATCH_ITEM_COUNT': 100,
        'FEED_FORMAT': 'csv',
        'FEED_URI': f"../../iii_results/%(batch_id)02d-{'_'.join(re.findall(r'[A-Z][^A-Z]*', __qualname__)[:-1]).lower()}.csv",
        'FEED_EXPORT_FIELDS': [
            'category',
            'subcategory_lvl1',
            'subcategory_lvl2',
            'page_url',
            'product_id',
            'image_url',
            'brand',
            'price',
            'title',
            'description',
            'gender',
        ]
    }

    def parse(self, response, **kwargs):
        data = response.xpath(Locators.DATA).get()
        raw_urls = re.findall(r'"url_key":"[a-zA-Z0-9_.+-]+', data)
        for url in raw_urls[:2]:
            url = 'https://www.flo.com.tr/' + url.split('"')[-1]

            yield scrapy.Request(url=url, callback=self.parse_subcategory)

        # pages_amount = response.xpath(Locators.PAGES_AMOUNT).get()
        # for page in range(2, pages_amount + 1):
        for page in range(2, 4):
            page_url = f'https://www.flo.com.tr/tum-kategoriler?page={page}'

            yield scrapy.Request(url=page_url, callback=self.parse)

    @staticmethod
    def parse_subcategory(response):
        items = FloComTrItem()

        data = response.xpath(Locators.ITEM_DATA).get()
        raw_special_price = re.findall(r'"special_price":\d{1,}[.,]?\d{1,}?', data)
        if raw_special_price is not None and raw_special_price == '':
            price = raw_special_price[0].split(':')[-1]
        else:
            raw_price = re.findall(r'"price":\d{1,}[.,]\d{1,}', data)
            if raw_price is not None and raw_price == '':
                price = raw_price[0].split(':')[-1]
            else:
                price = re.findall(r'\d{1,}[.,]\d{1,}', response.xpath(Locators.PRICE).get())

        category = response.xpath(Locators.CATEGORY).get()
        subcategory_lvl1 = response.xpath(Locators.SUBCATEGORY_LVL1).get()
        subcategory_lvl2 = response.xpath(Locators.SUBCATEGORY_LVL2).get()
        page_url = response.url
        product_id = response.url.split('-')[-1]
        image_url = response.xpath(Locators.IMAGE_URL).get()
        brand = response.xpath(Locators.BRAND).get()
        if brand is not None:
            brand = brand.strip()
        title = response.xpath(Locators.TITLE).get()
        if title is not None:
            title = title.strip()
        description = response.xpath(Locators.DESCRIPTION).get()
        if description is not None:
            description = description.strip()
        gender = response.xpath(Locators.GENDER).get()
        if gender is not None:
            gender = gender.strip()

        items['category'] = category
        items['subcategory_lvl1'] = subcategory_lvl1
        items['subcategory_lvl2'] = subcategory_lvl2
        items['page_url'] = page_url
        items['product_id'] = product_id
        items['image_url'] = image_url
        items['brand'] = brand
        items['price'] = price
        items['title'] = title
        items['description'] = description
        items['gender'] = gender

        yield items


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(FloComTrSpider)
    process.start()
