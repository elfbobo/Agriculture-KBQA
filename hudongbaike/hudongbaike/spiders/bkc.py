# -*- coding: utf-8 -*-
import scrapy


class BkcSpider(scrapy.Spider):
    name = 'bkc'
    allowed_domains = ['baike.com']

    def start_requests(self):
        pass

    def parse(self, response):
        pass
