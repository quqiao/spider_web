# -*- coding: utf-8 -*-
"""科欣医药网_药品专区"""
import scrapy
import time
from ScrapyPage.items import CrawlerwebItem
import json
from selenium import webdriver


class sckxyySpider(scrapy.Spider):
    name = 'scytyy_tjzq'
    allowed_domains = ['scytyy.com']
    start_urls = ['http://www.scytyy.net/login.html']
    custom_settings = {'ITEM_PIPELINES': {'ScrapyPage.pipelines.MysqlPipelinescytyy_tjzq': 300, }}
    headers = {'Host': 'www.scytyy.net',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
               }
    def start_requests(self):
        # url 来自于 <form method="post" id="loginForm" class="login-form" action="">
        # 中的 action
        url = 'http://www.scytyy.net/login.html'
        # data 的 key 来自于登录成功的跳转页，值为账号和密码
        data = {
            'username': '18030535053',
            'userpass': '123456',
            'do': 'login'
        }
        # scrapy.FormRequest() 用于提交 form 表单，post，用于登录
        request = scrapy.FormRequest(url=url, formdata=data, callback=self.parse_page)
        yield request

    def parse_page(self, response):
        # self.login()  # 首次使用，先执行login，保存cookies之后便可以注释，
        for i in range(1, 3):
            yxzq = 'http://www.scytyy.net/activitypage2.php'
            data = {
                'page': '%d' % i,
                'ajaxid': '605'
            }
            yield scrapy.FormRequest(url=yxzq, formdata=data, method='POST', headers=self.headers, callback=self.parse, dont_filter=True)

    def parse(self, response):
        # print("<<<<<<<<" + response.text)
        for i in range(1, 5):
            time.sleep(1)
            item = CrawlerwebItem()
            name = response.xpath('/html/body/ul/li[%d]/p[2]/a/text()' % i).extract()
            cj = response.xpath('/html/body/ul/li[%d]/p[3]/text()' % i).extract()
            gg = response.xpath('/html/body/ul/li[%d]/p[4]/text()' % i).extract()
            xq = response.xpath('/html/body/ul/li[%d]/p[5]/span[1]/text()' % i).extract()
            price = response.xpath('/html/body/ul/li[%d]/p[1]/span[1]/text()' % i).extract()
            item['name'] = name
            item['cj'] = cj
            item['gg'] = gg
            item['xq'] = xq
            item['price'] = price
            yield item


