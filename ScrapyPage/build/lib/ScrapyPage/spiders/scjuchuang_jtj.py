# -*- coding: utf-8 -*-
"""聚创医药网_院线专区"""
import scrapy
from scrapy import FormRequest,Request
import json
import time
from selenium import webdriver
from ScrapyPage.items import CrawlerwebItem

class ExampleLoginSpider(scrapy.Spider):
    name = 'scjuchuang_jtj'
    allowed_domains = ['scjuchuang']
    start_urls = ['https://www.scjuchuang.com/activeGroup?group_id=1382&sing=&page=1']
    custom_settings = {'ITEM_PIPELINES': {'ScrapyPage.pipelines.MysqlPipelinescjuchuang_jtj': 300, }}
    headers = {"Host": "www.scjuchuang.com",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"

    }

    # def login(self):
    #     driver = webdriver.Chrome(executable_path="C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe")
    #     login_url = 'https://www.scjuchuang.com/login'
    #     time.sleep(2)
    #     driver.get(login_url)
    #     username = driver.find_element_by_class_name('loginName')
    #     password = driver.find_element_by_class_name('loginPassword')
    #     username.send_keys('yczs123')
    #     password.send_keys('123456')
    #     # 模拟点击“登录”按钮
    #     driver.find_element_by_class_name('loginBtn').click()
    #     time.sleep(5)
    #     cookies = driver.get_cookies()
    #     driver.close()
    #     jsonCookies = json.dumps(cookies)  # 通过json将cookies写入文件
    #     with open('scjuchuangCookies.json', 'w') as f:
    #         f.write(jsonCookies)
    #     print(cookies)
    #
    # # scrapy请求的开始时start_request
    # def start_requests(self):
    #     self.login()  # 首次使用，先执行login，保存cookies之后便可以注释，
    #     for i in range(1, 3):
    #         tjzq = 'https://www.scjuchuang.com/activeGroup?group_id=1382&sing=&page=%d' % i
    #         # 毕竟每次执行都要登录还是挺麻烦的，我们要充分利用cookies的作用
    #         # 从文件中获取保存的cookies
    #         with open('scjuchuangCookies.json', 'r', encoding='utf-8') as f:
    #             listcookies = json.loads(f.read())  # 获取cookies
    #         # 把获取的cookies处理成dict类型
    #         cookies_dict = dict()
    #         for cookie in listcookies:
    #             # 在保存成dict时，我们其实只要cookies中的name和value，而domain等其他都可以不要
    #             cookies_dict[cookie['name']] = cookie['value']
    #         print(cookies_dict)
    #         # Scrapy发起其他页面请求时，带上cookies=cookies_dict即可，同时记得带上header值，
    #         yield scrapy.Request(url=tjzq, cookies=cookies_dict, callback=self.parse, headers=self.headers)

    def start_requests(self):
        for i in range(1, 3):
            zszq = "https://www.scjuchuang.com/activeGroup?group_id=1382&sing=&page=%d" % i
            yield scrapy.Request(url=zszq, callback=self.parse)

    def parse(self, response):
        # print(response.url)
        # print(response.body.decode('utf-8'))
        for i in range(1, 21):
            time.sleep(1)
            item = CrawlerwebItem()
            name = response.xpath('/html/body/div[8]/ul/li[%d]/div[3]/text()' % i).extract()
            cj = response.xpath('/html/body/div[8]/ul/li[%d]/p[1]/text()' % i).extract()
            gg = response.xpath('/html/body/div[8]/ul/li[%d]/p[2]/text()' % i).extract()
            xq = response.xpath('/html/body/div[8]/ul/li[%d]/p[3]/span[1]/text()' % i).extract()
            price = response.xpath('/html/body/div[8]/ul/li[%d]/div[1]/div/div[1]/div[2]/b/text()' % i).extract()

            item['name'] = name
            item['cj'] = cj
            item['gg'] = gg
            item['xq'] = xq
            item['price'] = price
            yield item



