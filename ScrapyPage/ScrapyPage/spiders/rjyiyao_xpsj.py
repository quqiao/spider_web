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
    # custom_settings = {'ITEM_PIPELINES': {'ScrapyPage.pipelines.MysqlPipelinerjyiyao_xpsj': 300}}

    headers = {"Host": "new.rjyiyao.com",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
               }

    def login(self):
        driver = webdriver.Chrome(
            executable_path="C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe")
        login_url = 'http://new.rjyiyao.com/web/login'
        driver.get(login_url)
        username = driver.find_element_by_id('username')
        password = driver.find_element_by_id('password')
        username.send_keys('18030535053')
        password.send_keys('123456')
        # 模拟点击“登录”按钮
        driver.find_element_by_id('btnLogin').click()
        time.sleep(20)
        # cookies = self.get_cookies()
        # driver.close()
        # jsonCookies = json.dumps(cookies)  # 通过json将cookies写入文件
        # with open('rjyiyaoCookies.json', 'w') as f:
        #     f.write(jsonCookies)
        # print(cookies)

    # scrapy请求的开始时start_request
    def start_requests(self,):
        self.login()  # 首次使用，先执行login，保存cookies之后便可以注释，
        for i in range(1, 10):
            xpsj = 'http://new.rjyiyao.com/web/product/group/5?page=%d' % i
            # driver.get(xpsj)
            time.sleep(10)
            yield scrapy.Request(url=xpsj, callback=self.parse)

    def parse(self, response):
        for i in range(1, 10):
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

# class rjyiyaoSpider(scrapy.Spider):
#     name = 'rjyiyao_xpsj'
#     allowed_domains = ['rjyiyao']
#     start_urls = ['http://new.rjyiyao.com/web/product/group/5']
#     custom_settings = {'ITEM_PIPELINE': {'ScrapyPage.pipelines.MysqlPipelinerjyiyao_xpsj': 200}}
#     header = {'Connection': 'keep-alive',
#               'Host': 'new.rjyiyao.com',
#               'Referer': 'http://new.rjyiyao.com/web/login',
#               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
#               }
#     def page_parse(self, response):
#         # print(response.text)
#         for i in range(1, 5):
#             time.sleep(1)
#             item = CrawlerwebItem()
#             name = response.xpath('//*[@id="pageContent"]/div/div[%d]/h1/text()' % i).extract()
#             cj = response.xpath('//*[@id="pageContent"]/div/div[%d]/p/text()' % i).extract()
#             gg = response.xpath('//*[@id="pageContent"]/div/div[%d]/section[1]/p[1]/text()' % i).extract()
#             xq = response.xpath('//*[@id="pageContent"]/div/div[%d]/section[2]/p[1]/text()' % i).extract()
#             price = response.xpath('//*[@id="pageContent"]/div/div[%d]/h2/span/text()' % i).extract()
#             item['name'] = name
#             item['cj'] = cj
#             item['gg'] = gg
#             item['xq'] = xq
#             item['price'] = price
#             yield item
#
#     def start_requests(self):
#         return [scrapy.Request(url='http://new.rjyiyao.com/web/login', headers=self.header, callback=self.login)]
#
#     def login(self, response):
#         driver = webdriver.Chrome(executable_path="C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe")
#         driver.get("http://new.rjyiyao.com/web/login")
#         username = driver.find_element_by_id('username')
#         password = driver.find_element_by_id('password')
#         username.send_keys('18030535053')
#         password.send_keys('123456')
#         #模拟点击“登录”按钮
#         driver.find_element_by_id('btnLogin').click()
#         driver.get("http://new.rjyiyao.com/web/product/group/5")
#         time.sleep(5)
#         cookie_dict = {}
#         cookies = driver.get_cookies()
#         for cookie in cookies:
#             cookie_dict[cookie['name']] = cookie['value']


