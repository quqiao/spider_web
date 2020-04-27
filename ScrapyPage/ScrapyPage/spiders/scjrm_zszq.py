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
    start_urls = ["http://www.scjrm.com/zs/index.html?page=1"]
    # login_url = 'http://www.scjrm.com/site/login.html'
    # custom_settings = {'ITEM_PIPELINES': {'ScrapyPage.pipelines.MysqlPipelinescjrm_zszq': 300, }}
    headers = {"Host": "http://www.scjrm.com",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    }

    def login(self):
        login_url = 'http://www.scjrm.com/site/login.html'
        driver = webdriver.Chrome(executable_path="C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe")
        driver.get(login_url)
        username = driver.find_element_by_id('phonenumber')
        password = driver.find_element_by_id('password')
        username.send_keys('18030535053')
        password.send_keys('123456')
        #模拟点击“登录”按钮
        driver.find_element_by_id('sub_bt').click()
        time.sleep(15)
        cookies = driver.get_cookies()
        driver.close()
        jsonCookies = json.dumps(cookies)  # 通过json将cookies写入文件
        with open('scjrmCookies.json', 'w') as f:
            f.write(jsonCookies)
        print(cookies)

    # scrapy请求的开始时start_request
    def start_requests(self):
        zszq = 'http://www.scjrm.com/zs/index.html?page=1'
        # self.login()  # 首次使用，先执行login，保存cookies之后便可以注释，
        # 毕竟每次执行都要登录还是挺麻烦的，我们要充分利用cookies的作用
        # 从文件中获取保存的cookies
        with open('scjrmCookies.json', 'r', encoding='utf-8') as f:
            listcookies = json.loads(f.read())  # 获取cookies
        # 把获取的cookies处理成dict类型
        cookies_dict = dict()
        for cookie in listcookies:
            # 在保存成dict时，我们其实只要cookies中的name和value，而domain等其他都可以不要
            cookies_dict[cookie['name']] = cookie['value']
        print(cookies_dict)
        # Scrapy发起其他页面请求时，带上cookies=cookies_dict即可，同时记得带上header值，
        yield scrapy.Request(url=zszq, cookies=cookies_dict, callback=self.parse, headers=self.headers)

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
        next_page = response.xpath('/html/body/div[2]/div[2]/div[2]/span[12]/a/@href').extract_first()
        print(next_page)
        if next_page is not None:
            next_page1 = response.urljoin(next_page)
            yield scrapy.Request(url=next_page1, callback=self.parse, dont_filter=True)

    # # 方式一：注意execute的参数类型为一个列表
    # cmdline.execute('scrapy crawl spidername'.split())
    # # 方式二:注意execute的参数类型为一个列表
    # cmdline.execute(['scrapy', 'crawl', 'spidername'])
    # 方式三：execute执行本脚本
    # now = time.strftime("%Y-%m-%d")
    # cmdline.execute('scrapy crawl longyi_tjzq -o longyi_tjzq_%s -s FEED_EXPORT_ENCODING=UTF-8' % now)


