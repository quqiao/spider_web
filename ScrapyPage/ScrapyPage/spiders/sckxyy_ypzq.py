# -*- coding: utf-8 -*-
"""科欣医药网_药品专区"""
import scrapy
import time
from ScrapyPage.items import CrawlerwebItem
import json
from selenium import webdriver


class sckxyySpider(scrapy.Spider):
    name = 'sckxyy_ypzq'
    allowed_domains = ['sckxyy.com']
    start_urls = ['http://www.sckxyy.com/Login.html', 'http://www.sckxyy.com/Drug_zone.html']
    custom_settings = {'ITEM_PIPELINES': {'ScrapyPage.pipelines.MysqlPipelinesckxyy_ypzq': 300, }}
    headers = {'Host': 'www.sckxyy.com',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
               }

    def login(self):
        driver = webdriver.Chrome(executable_path="C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe")
        login_url = 'http://www.sckxyy.com/Login.html'
        driver.get(login_url)
        time.sleep(2)
        username = driver.find_element_by_id('usernameLogin')
        password = driver.find_element_by_id('passwordLogin')
        username.send_keys('bianyuantianshi')
        password.send_keys('123456')
        # 模拟点击“登录”按钮
        driver.find_element_by_id('userLogin').click()
        time.sleep(5)
        cookies = driver.get_cookies()
        driver.close()
        jsonCookies = json.dumps(cookies)  # 通过json将cookies写入文件
        with open('sckxyyCookies.json', 'w') as f:
            f.write(jsonCookies)
        print(cookies)

    def start_requests(self):
        # self.login()  # 首次使用，先执行login，保存cookies之后便可以注释，
        for i in range(1, 3):
            yxzq = 'http://www.sckxyy.com/goodsGroup_findFifthAnniversaryGoods'
            data = {
                'page': '%d' % i,
                'rows': '25',
                'p': '2'
            }
            with open('sckxyyCookies.json', 'r', encoding='utf-8') as f:
                listcookies = json.loads(f.read())  # 获取cookies
            # 把获取的cookies处理成dict类型
            cookies_dict = dict()
            for cookie in listcookies:
                # 在保存成dict时，我们其实只要cookies中的name和value，而domain等其他都可以不要
                cookies_dict[cookie['name']] = cookie['value']
            yield scrapy.FormRequest(url=yxzq, formdata=data, cookies=cookies_dict, method='POST', headers=self.headers, callback=self.parse, dont_filter=True)

    def parse(self, response):
        print("<<<<<<<<" + response.text)
        res = json.loads(response.text)
        for i in range(1, 10):
            time.sleep(1)
            item = CrawlerwebItem()
            name = res[int(i)]['name']
            cj = res[int(i)]['production']
            gg = res[int(i)]['norms']
            xq = res[int(i)]['exp']
            price = res[int(i)]['wholesale']
            item['name'] = name
            item['cj'] = cj
            item['gg'] = gg
            item['xq'] = xq
            item['price'] = price
            yield item


