# -*- coding: utf-8 -*-
"""金仁药淘齐_诊所专区"""
import scrapy
import time
from ScrapyPage.items import CrawlerwebItem
from selenium import webdriver
from scrapy.http import HtmlResponse



class scjrm_zszqSpider(scrapy.Spider):
    name = 'scjrm_zszq'
    allowed_domains = ['scjrm']
    start_urls = ["http://www.scjrm.com/zs/index.html?page=1"]
    # login_url = 'http://www.scjrm.com/site/login.html'
    custom_settings = {'ITEM_PIPELINES': {'ScrapyPage.pipelines.MysqlPipelinescjrm_zszq': 300, }}

    # def __init__(self):
    #     super().__init__()
    #     driver = None  # 实例selenium
    #     cookies = None  # 用来保存cookie

    def parse(self, response):
        # print(response.url)
        # print(response.body.decode('utf-8'))
        for i in range(1, 5):
            time.sleep(1)
            item = CrawlerwebItem()
            name = response.xpath('/html/body/div[2]/div[2]/div[1]/ul/li[%d]/p[1]/text()' % i).extract()
            cj = response.xpath('/html/body/div[2]/div[2]/div[1]/ul/li[%d]/p[2]/text()' % i).extract()
            price = response.xpath('/html/body/div[2]/div[2]/div[1]/ul/li[%d]/p[3]/span/text()' % i).extract()
            item['name'] = name
            item['cj'] = cj
            item['price'] = price
            yield item
        # next_page = response.xpath('/html/body/div[2]/div[2]/div[2]/span[12]/a/@href').extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        # yield scrapy.Request(url=next_page, callback=self.parse, dont_filter=True)

    # # 方式一：注意execute的参数类型为一个列表
    # cmdline.execute('scrapy crawl spidername'.split())
    # # 方式二:注意execute的参数类型为一个列表
    # cmdline.execute(['scrapy', 'crawl', 'spidername'])
    # 方式三：execute执行本脚本
    # now = time.strftime("%Y-%m-%d")
    # cmdline.execute('scrapy crawl longyi_tjzq -o longyi_tjzq_%s -s FEED_EXPORT_ENCODING=UTF-8' % now)


