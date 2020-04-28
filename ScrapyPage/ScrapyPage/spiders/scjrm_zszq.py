# -*- coding: utf-8 -*-
"""金仁药淘齐_诊所专区"""
import scrapy
import time
import json
from ScrapyPage.items import CrawlerwebItem
from selenium import webdriver
from scrapy.http import HtmlResponse



class scjrm_zszqSpider(scrapy.Spider):
    name = 'scjrm_zszq'
    allowed_domains = ['www.scjrm.com']
    # start_urls = ["http://www.scjrm.com/site/login.html"]
    # login_url = 'http://www.scjrm.com/site/login.html'
    # custom_settings = {'ITEM_PIPELINES': {'ScrapyPage.pipelines.MysqlPipelinescjrm_zszq': 300, }}
    # scrapy请求的开始时start_request
    def start_requests(self):
        for i in range(1, 5):
            zszq = "http://www.scjrm.com/zs/index.html?page=%d" % i
            yield scrapy.Request(url=zszq, callback=self.parse)

    def parse(self, response):
        # print(response.url)
        # print(response.body.decode('utf-8'))
        for i in range(1, 5):
            item = CrawlerwebItem()
            name = response.xpath('/html/body/div[2]/div[2]/div[1]/ul/li[%d]/p[1]/text()' % i).extract()
            cj = response.xpath('/html/body/div[2]/div[2]/div[1]/ul/li[%d]/p[2]/text()' % i).extract()
            price = response.xpath('/html/body/div[2]/div[2]/div[1]/ul/li[%d]/p[3]/span/text()' % i).extract()
            item['name'] = name
            item['cj'] = cj
            item['price'] = price
            yield item


    # # 方式一：注意execute的参数类型为一个列表
    # cmdline.execute('scrapy crawl spidername'.split())
    # # 方式二:注意execute的参数类型为一个列表
    # cmdline.execute(['scrapy', 'crawl', 'spidername'])
    # 方式三：execute执行本脚本
    # now = time.strftime("%Y-%m-%d")
    # cmdline.execute('scrapy crawl longyi_tjzq -o longyi_tjzq_%s -s FEED_EXPORT_ENCODING=UTF-8' % now)


