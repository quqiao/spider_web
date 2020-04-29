# -*- coding: utf-8 -*-
"""科欣医药网_药品专区"""
import scrapy
import time
from ScrapyPage.items import CrawlerwebItem
import json
from selenium import webdriver


class sckxyySpider(scrapy.Spider):
    name = 'sckxyy_ypzq'
    allowed_domains = ['sckxyy.com']
    start_urls = ['http://www.sckxyy.com/Login.html', 'http://www.sckxyy.com/Drug_zone.html']
    # custom_settings = {'ITEM_PIPELINES': {'ScrapyPage.pipelines.MysqlPipelinesckxyy_ypzq': 300, }}


    def parse(self, response):
        for i in range(1, 5):
            time.sleep(1)
            item = CrawlerwebItem()
            name = response.xpath('//*[@id="special-zoneT"]/div[%d]/a/h1/span/text()' % i).extract()
            cj = response.xpath('//*[@id="special-zoneT"]/div[%d]/a/section/p[1]/text()' % i).extract()
            gg = response.xpath('//*[@id="special-zoneT"]/div[%d]/a/section/p[2]/text()' % i).extract()
            xq = response.xpath('//*[@id="special-zoneT"]/div[%d]/a/section/div[1]/p[1]/text()' % i).extract()
            price = response.xpath('//*[@id="special-zoneT"]/div[%d]/a/section/div[2]/p[1]/span/text()' % i).extract()
            item['name'] = name
            item['cj'] = cj
            item['gg'] = gg
            item['xq'] = xq
            item['price'] = price
            yield item


