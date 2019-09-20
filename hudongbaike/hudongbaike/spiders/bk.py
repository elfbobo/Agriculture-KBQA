# -*- coding: utf-8 -*-
import scrapy


class BkSpider(scrapy.Spider):
    name = 'bk'
    allowed_domains = ['so.baike.com']
    start_urls = ['http://so.baike.com/']

    def parse(self, response):
        pass
