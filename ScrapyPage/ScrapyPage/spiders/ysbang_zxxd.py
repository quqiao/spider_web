# -*- coding: utf-8 -*-
"""药师帮_在线下单"""
import scrapy
import time
from ScrapyPage.items import CrawlerwebItem
import urllib.request

class RenrenLoginSpider(scrapy.Spider):
    name = 'ysbang_zxxd'
    allowed_domains = ['www.ysbang.cn/']
    start_urls = ['https://dian.ysbang.cn/index.html#/indexContent']

    def start_requests(self):
        # url 来自于 <form method="post" id="loginForm" class="login-form" action="">
        # 中的 action
        url = 'https://dian.ysbang.cn/index.html#/login'
        # data 的 key 来自于登录成功的跳转页，值为账号和密码
        data = {
            'userAccount': '13518134160',
            'password': 'da674dad3600d948933d47dc69da162f',
            'ex': '201909051538',
            'identification': 'JUL7',
            'platform': 'pc',
            'rememberMe': 'on',
            'ua': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 Chrome 76',
            'version': '4.29.0'
        }
        # scrapy.FormRequest() 用于提交 form 表单，post，用于登录
        request = scrapy.FormRequest(url=url, formdata=data, callback=self.parse_page)
        yield request

    def parse_page(self, response):
        # 为了验证登陆成功，查看在线下单
        print("<<<<<" + response.text)
        request = scrapy.Request(url='https://dian.ysbang.cn/index.html#/indexContent', callback=self.parse_profile, dont_filter=True)
        yield request

    def parse_profile(self, response):
        yzm = response.xpath('//*[@id="captchaImg"]/src').extract()
        location = 'F:/pyhcarm/ScrapyPage/ScrapyPage/yzm/yzm.jpg'
        urllib.request.urlretrieve(yzm[0], filename=location)
        captcha_value = input()
        # print(response.text)
        for i in range(1, 21):
            time.sleep(1)
            item = CrawlerwebItem()
            name = response.xpath('//*[@id="wrapper"]/div[4]/div/div[%d]/div[2]/div[2]/span[4]/text()' % i).extract()
            cj = response.xpath('//*[@id="wrapper"]/div[4]/div/div[%d]/div[2]/div[4]/text()' % i).extract()
            xq = response.xpath('//*[@id="wrapper"]/div[4]/div/div[%d]/div[1]/div[2]/div/text()' % i).extract()
            price = response.xpath('//*[@id="wrapper"]/div[4]/div/div[1]/div[2]/div[1]/strong/text()' % i).extract()
            item['name'] = name
            item['cj'] = cj
            item['xq'] = xq
            item['price'] = price
            yield item
        # next = response.css('body > div:nth-child(8) > div > div.pagers > a:nth-child(11)::attr(href)').extract_first()
        # url = response.urljoin(next)
        # yield scrapy.Request(url=url, callback=self.parse)


