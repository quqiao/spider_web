# -*- coding: utf-8 -*-
"""嘉事蓉锦医药网_新品上架"""
import scrapy
import time
from ScrapyPage.items import CrawlerwebItem
from selenium import webdriver
import json
from scrapy.http import HtmlResponse


class rjyiyaoSpider(scrapy.Spider):
    name = 'rjyiyao_xpsj'
    allowed_domains = ['rjyiyao']
    # start_urls = ['http://new.rjyiyao.com/web/product/group/5']
    custom_settings = {'ITEM_PIPELINES': {'ScrapyPage.pipelines.MysqlPipelinerjyiyao_xpsj': 300}}

    # scrapy请求的开始时start_request
    def start_requests(self):
        for i in range(1, 4):
            zszq = "http://new.rjyiyao.com/web/product/group/5?page=%d" % i
            yield scrapy.Request(url=zszq, callback=self.parse)

    def parse(self, response):
        # print("<<<<<<<<<<<<<<<<<<" + response.text)
        for i in range(1, 5):
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



