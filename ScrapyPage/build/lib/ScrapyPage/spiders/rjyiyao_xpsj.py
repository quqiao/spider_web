# -*- coding: utf-8 -*-
"""嘉事蓉锦医药网_新品上架"""
import scrapy
import time
from ScrapyPage.items import CrawlerwebItem
from selenium import webdriver


class rjyiyaoSpider(scrapy.Spider):
    name = 'rjyiyao_xpsj'
    allowed_domains = ['rjyiyao']
    start_urls = ['http://new.rjyiyao.com/web/product/group/5']
    custom_settings = {'ITEM_PIPELINE': {'ScrapyPage.pipelines.MysqlPipelinerjyiyao_xpsj': 200}}

    def __init__(self):
        super().__init__()
        driver = None  # 实例selenium
        cookies = None  # 用来保存cookie

    def parse(self, response):
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
        # next_page = response.xpath('/html/body/div[4]/div/div[5]/a[11]/@href').extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)

    # # 方式一：注意execute的参数类型为一个列表
    # cmdline.execute('scrapy crawl spidername'.split())
    # # 方式二:注意execute的参数类型为一个列表
    # cmdline.execute(['scrapy', 'crawl', 'spidername'])
    # 方式三：execute执行本脚本
    # now = time.strftime("%Y-%m-%d")
    # cmdline.execute('scrapy crawl longyi_tjzq -o longyi_tjzq_%s -s FEED_EXPORT_ENCODING=UTF-8' % now)
