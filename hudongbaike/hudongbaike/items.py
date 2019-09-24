# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HudongbaikeItem(scrapy.Item):
    id = scrapy.Field()
    intro = scrapy.Field()
    attr_data = scrapy.Field()
    base_info = scrapy.Field()
    name = scrapy.Field()