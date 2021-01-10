# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FloComTrItem(scrapy.Item):
    category = scrapy.Field()
    subcategory_lvl1 = scrapy.Field()
    subcategory_lvl2 = scrapy.Field()
    page_url = scrapy.Field()
    product_id = scrapy.Field()
    image_url = scrapy.Field()
    brand = scrapy.Field()
    price = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    gender = scrapy.Field()
