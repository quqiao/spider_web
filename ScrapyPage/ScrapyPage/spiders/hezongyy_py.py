# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import FormRequest, Request
from ScrapyPage.items import CrawlerwebItem
import time
import scrapy
# from scrapy import FormRequest,Request
pass

class ExampleLoginSpider(scrapy.Spider):
    name = "hezongyy_py"
    allowed_domains = ['www.hezongyy.com']
    custom_settings = {'ITEM_PIPELINES': {'ScrapyPage.pipelines.MysqlPipelinehezongyy_py': 300, }}
    # start_urls = ['https://www.hezongyy.com/puyao.html']
    # login_url = 'https://www.hezongyy.com/auth/login'


    def start_requests(self):
        for i in range(1, 3):
            url_py = "https://www.hezongyy.com/puyao.html?order=DESC&pageNumber=%d" % i
            yield scrapy.Request(url=url_py, callback=self.parse)

    def parse(self, response):
        # print(response.text)
        for i in range(1, 3):
            time.sleep(1)
            item = CrawlerwebItem()
            name = response.css('#datu > div > ul > li:nth-child(%d) > div.datu-mingzi::text' % i).extract()
            cj = response.xpath('//*[@id="datu"]/div/ul/li[%d]/div[4]/text()' % i).extract()
            gg = response.xpath('//*[@id="datu"]/div/ul/li[%d]/div[5]/span/text()' % i).extract()
            xq = response.xpath('//*[@id="datu"]/div/ul/li[%d]/div[6]/span[1]/text()' % i).extract()
            price = response.xpath('//*[@id="datu"]/div/ul/li[%d]/div[2]/text()' % i).extract()
            item['name'] = name
            item['cj'] = cj
            item['gg'] = gg
            item['xq'] = xq
            item['price'] = price
            yield item


