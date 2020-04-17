# -*- coding: utf-8 -*-
"""粤通医药网_诊所专区"""
import scrapy
import time
from ScrapyPage.items import CrawlerwebItem


class RenrenLoginSpider(scrapy.Spider):
    name = 'scytyy_zszq'
    allowed_domains = ['www.scytyy.net']
    start_urls = ['http://www.scytyy.net/goods-zs.html']

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
        # 为了验证登陆成功，查看诊所专区
        request = scrapy.Request(url='http://www.scytyy.net/goods-zs.html', callback=self.parse_profile, dont_filter=True)
        yield request

    def parse_profile(self, response):
        # print(response.text)
        for i in range(1, 5):
            time.sleep(1)
            item = CrawlerwebItem()
            name = response.xpath('//*[@id="pro_list1"]/li[%d]/p[2]/a/text()' % i).extract()
            cj = response.xpath('//*[@id="pro_list1"]/li[%d]/p[3]/text()' % i).extract()
            gg = response.xpath('//*[@id="pro_list1"]/li[%d]/p[4]/text()' % i).extract()
            xq = response.xpath('//*[@id="pro_list1"]/li[%d]/p[5]/text()' % i).extract()
            price = response.xpath('//*[@id="pro_list1"]/li[%d]/p[1]/span[1]/span/text()' % i).extract()
            item['name'] = name
            item['cj'] = cj
            item['gg'] = gg
            item['xq'] = xq
            item['price'] = price
            yield item
        # next = response.css('body > div:nth-child(8) > div > div.pagers > a:nth-child(11)::attr(href)').extract_first()
        # url = response.urljoin(next)
        # yield scrapy.Request(url=url, callback=self.parse)


