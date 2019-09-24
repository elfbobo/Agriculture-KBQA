# -*- coding: utf-8 -*-
from hudongbaike.items import HudongbaikeItem
from tqdm import tqdm
import scrapy
import pandas as pd
import hashlib


class BkcSpider(scrapy.Spider):
    name = 'bkc'
    allowed_domains = ['baike.com']

    def start_requests(self):
        df = pd.read_csv("../data/query_list.csv", header=None)
        with tqdm(total=df.shape[0]) as pbar:
            for row in df.itertuples(index=True, name='Pandas'):
                name, url = getattr(row, "_1"), getattr(row, "_2")
                pbar.update(1)
                yield scrapy.Request(url, callback=self.parse, meta={"name": name})

    def parse(self, response):
        item = HudongbaikeItem()
        summary = response.xpath('//div[@class="summary"]//p//text()').extract()
        # 获取基本简介
        item["intro"] = "".join(summary).strip()
        attribute_ = '//div[@class="module zoom"]/table//strong[contains(text(),"：")]/parent::td'
        base_item_ = response.xpath(attribute_)
        attr_data = {}
        # 获取详细属性
        name = response.meta["name"]
        for node in base_item_:
            key = "".join(node.xpath("./strong//text()").extract()).strip().replace("：", "")
            value = "".join(node.xpath("./span//text()").extract()).strip()
            attr_data[key] = value
        item["attr_data"] = attr_data
        item["id"] = hashlib.md5(name.encode('utf-8')).hexdigest()
        item["name"] = name
        # 获取详细信息
        content = response.xpath('//div[@id="content"]//text()').extract()
        title = response.xpath(
            '//div[@class="content_h2 bac_no" or @class="content_h2"]//a[not(@class="bjbd")]/following-sibling::text()'
        ).extract()
        title = [k for k in title if k != '\n' and k != '\t']
        key_idxs = [content.index(k) for k in title]
        key_idxs.append("")
        key_idxs_zip = list(zip(key_idxs[:-1], key_idxs[1:]))
        content_chunk = ["".join(content[start + 1:]) if end == "" else "".join(content[start + 1: end]) for start, end
                         in key_idxs_zip]
        base_info = dict(zip(title, content_chunk))
        item["base_info"] = base_info
        yield item
