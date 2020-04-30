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
    headers = {'Host': 'www.sckxyy.com',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
               }

    def start_requests(self):
        # self.login()  # 首次使用，先执行login，保存cookies之后便可以注释，
        for i in range(1, 3):
            yxzq = 'http://www.sckxyy.com/goodsGroup_findFifthAnniversaryGoods'
            data = {
                'page': "3",
            }
            yield scrapy.FormRequest(url=yxzq, method='POST',headers=self.headers, callback=self.parse, dont_filter=True)

    def parse(self, response):
        print("<<<<<<<<" + response.text)
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


