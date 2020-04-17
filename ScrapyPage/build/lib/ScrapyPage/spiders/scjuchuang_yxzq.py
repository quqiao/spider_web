# -*- coding: utf-8 -*-
"""聚创医药网_院线专区"""
import scrapy
from scrapy import FormRequest,Request
import json
import time
from ScrapyPage.items import CrawlerwebItem

class ExampleLoginSpider(scrapy.Spider):
    name = 'scjuchuang_yxzq'
    allowed_domains = ['scjrm']
    start_urls = ['http://www.scjrm.com/zs/index.html']

    def __init__(self):
        super().__init__()
        driver = None  # 实例selenium
        cookies = None  # 用来保存cookie


    def parse(self, response):
        # print(response.url)
        # print(response.body.decode('utf-8'))
        for i in range(1, 5):
            time.sleep(1)
            item = CrawlerwebItem()
            name = response.xpath('/html/body/div[8]/ul/li[%d]/div[3]/text()' % i).extract()
            cj = response.xpath('/html/body/div[8]/ul/li[%d]/p[1]/text()' % i).extract()
            gg = response.xpath('/html/body/div[8]/ul/li[%d]/p[2]/text()' % i).extract()
            xq = response.xpath('/html/body/div[8]/ul/li[%d]/p[3]/span[1]/text()' % i).extract()
            price = response.xpath('/html/body/div[8]/ul/li[%d]/div[1]/p/span[2]/text()' % i).extract()
            item['name'] = name
            item['cj'] = cj
            item['gg'] = gg
            item['xq'] = xq
            item['price'] = price
            yield item



