# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from pandas.io.json import json_normalize
import json
from urllib.parse import quote, unquote


class BkSpider(scrapy.Spider):
    name = 'bk'
    allowed_domains = ['baike.com']

    def start_requests(self):
        base_urls = [
            'http://fenlei.baike.com/categorySpecialTopicAction.do?action=showDocInfo&categoryName={}&pagePerNum=200',
            'http://fenlei.baike.com/{}/list/'
        ]
        for query in ["植物", "水果", "蔬菜", "花卉", "农作物", "绿色植物", "有毒植物"]:
            query = quote(query.encode('utf-8'))
            for url in base_urls:
                yield scrapy.Request(url.format(query))

    def parse(self, response):
        if "action=showDocInfo" in response.url:
            rsp = json.loads(response.text)
            df = json_normalize(rsp["list"])
            df = df[["title", "title_url"]]
        else:
            node_list = response.xpath('//dl[@class="link_blue line-25 zoom"]//dd/a[@target="_blank"]')
            elm_list = []
            for node in node_list:
                title, url = node.xpath('./text()').extract_first(), node.xpath('./@href').extract_first()
                elm_list.append([title, url])
            df = pd.DataFrame(elm_list)
        df.to_csv("../data/query_list.csv", index=False, header=None, mode='a')
