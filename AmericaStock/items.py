# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmericastockItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    symbol = scrapy.Field()
    name = scrapy.Field()
    current = scrapy.Field()
    chg = scrapy.Field()
    market_capital = scrapy.Field()
    pe_ttm = scrapy.Field()
    pass
