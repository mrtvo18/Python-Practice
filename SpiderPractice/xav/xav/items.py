# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XavItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    file = scrapy.Field()
    url = scrapy.Field()
