# -*- coding: utf-8 -*-
"""嘉事蓉锦医药网_新品上架"""
import scrapy
import time
from ScrapyPage.items import CrawlerwebItem
from selenium import webdriver
from scrapy.http import HtmlResponse


class rjyiyaoSpider(scrapy.Spider):
    name = 'rjyiyao_zkzq'
    allowed_domains = ['rjyiyao']
    start_urls = ['http://new.rjyiyao.com/web/product/sale/3?page=1']
    custom_settings = {'ITEM_PIPELINES': {'ScrapyPage.pipelines.MysqlPipelinerjyiyao_zkzq': 300}}

    def start_requests(self):
        for i in range(1, 3):
            zszq = "http://new.rjyiyao.com/web/product/sale/3?page=%d" % i
            yield scrapy.Request(url=zszq, callback=self.parse)

    def parse(self, response):
        for i in range(1, 6):
            time.sleep(1)
            item = CrawlerwebItem()
            name = response.xpath('//*[@id="pageContent"]/div/div[%d]/h1/text()' % i).extract()
            cj = response.xpath('//*[@id="pageContent"]/div/div[%d]/p/text()' % i).extract()
            gg = response.xpath('//*[@id="pageContent"]/div/div[%d]/section[1]/p[1]/text()' % i).extract()
            xq = response.xpath('//*[@id="pageContent"]/div/div[%d]/section[2]/p[1]/text()' % i).extract()
            price = response.xpath('//*[@id="pageContent"]/div/div[%d]/h2/span/text()' % i).extract()
            item['name'] = name
            item['cj'] = cj
            item['gg'] = gg
            item['xq'] = xq
            item['price'] = price
            yield item



