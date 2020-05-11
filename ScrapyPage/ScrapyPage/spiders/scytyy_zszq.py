# -*- coding: utf-8 -*-
"""粤通医药网_诊所专区"""
import scrapy
import time
from ScrapyPage.items import CrawlerwebItem


class scytyySpider(scrapy.Spider):
    name = 'scytyy_zszq'
    allowed_domains = ['www.scytyy.net']
    start_urls = ['http://www.scytyy.net/goods-zs.html']
    custom_settings = {'ITEM_PIPELINES': {'ScrapyPage.pipelines.MysqlPipelinescytyy_zszq': 300, }}

    # def start_requests(self):
    #     # url 来自于 <form method="post" id="loginForm" class="login-form" action="">
    #     # 中的 action
    #     url = 'http://www.scytyy.net/login.html'
    #     # data 的 key 来自于登录成功的跳转页，值为账号和密码
    #     data = {
    #         'username': '18030535053',
    #         'userpass': '123456',
    #         'do': 'login'
    #     }
    #     # scrapy.FormRequest() 用于提交 form 表单，post，用于登录
    #     request = scrapy.FormRequest(url=url, formdata=data, callback=self.parse_page)
    #     yield request
    #
    # def parse_page(self, response):
    #     print(response.text)
    #     # 为了验证登陆成功，查看诊所专区
    #     request = scrapy.Request(url='http://www.scytyy.net/goods-zs.html', callback=self.parse_profile, dont_filter=True)
    #     yield request

    def start_requests(self):
        for i in range(1, 3):
            zszq = "http://www.scytyy.net/goods-zs-filter-0-0-0-0-0-0-0-1-1-%d,.html" % i
            yield scrapy.Request(url=zszq, callback=self.parse)

    def parse(self, response):
        # print(response.text)
        for i in range(1, 3):
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
        # next_page = response.xpath("//*[text()='下一页']/@href").extract_first()
        # if next_page is not None:
        #     next_page1 = response.urljoin(next_page)
        #     yield scrapy.Request(next_page1, callback=self.parse_profile)



