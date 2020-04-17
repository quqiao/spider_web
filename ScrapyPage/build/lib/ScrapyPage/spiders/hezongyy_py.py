# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import FormRequest, Request
from ScrapyPage.items import CrawlerwebItem
import time
import scrapy
# from scrapy import FormRequest,Request
pass

# class ExampleLoginSpider(scrapy.Spider):
#     name = "hezongyy_py"
#     allowed_domains = ['www.hezongyy.com']
#     start_urls = ['https://www.hezongyy.com/puyao.html']
#     # login_url = 'https://www.hezongyy.com/auth/login'
#
#
#     def start_requests(self):
#         # url 来自于 <form method="post" id="loginForm" class="login-form" action="http://www.renren.com/PLogin.do">
#         # 中的 action
#         url = 'https://www.hezongyy.com/auth/login'
#         # data 的 key 来自于登录成功的跳转页，值为账号和密码
#         data = {
#                 # "act": "ajax_act_login",
#                 "user_name": "test",
#                 "password": "123456",
#                 # "back_act": "/index.php",
#                 # "remember": 1
#         }
#         # scrapy.FormRequest() 用于提交 form 表单，post，用于登录
#         request = scrapy.FormRequest(url=url, formdata=data, callback=self.parse_page)
#         yield request
#
#     def parse_page(self, response):
#         # 为了验证登陆成功，查看别人的人人主页
#         request = scrapy.Request(url='https://www.hezongyy.com/puyao.html', callback=self.parse_profile, dont_filter=True)
#         yield request
#
#     def parse_profile(self, response):
#         print(response.text)

        # for i in range(1, 3):
        #     time.sleep(5)
        #     item = CrawlerwebItem()
        #     name = response.css('#datu > div > ul > li:nth-child(%d) > div.datu-mingzi::text' % i).extract()
        #     cj = response.xpath('//*[@id="datu"]/div/ul/li[%d]/div[4]/text()' % i).extract()
        #     gg = response.xpath('//*[@id="datu"]/div/ul/li[%d]/div[5]/span/text()' % i).extract()
        #     xq = response.xpath('//*[@id="datu"]/div/ul/li[%d]/div[6]/span[1]/text()' % i).extract()
        #     price = response.xpath('//*[@id="datu"]/div/ul/li[%d]/div[2]/text()' % i).extract()
        #     item['name'] = name
        #     item['cj'] = cj
        #     item['gg'] = gg
        #     item['xq'] = xq
        #     item['price'] = price
        #     yield item
    # def start_requests(self):
    #     yield scrapy.Request(self.login_url, callback=self.login)
    #
    # def login(self, response):
    #     formdata = {"act": "ajax_act_login",
    #                 "user_name": "test",
    #                 "password": "123456",
    #                 "back_act": "/index.php",
    #                 "remember": "1"
    #                 }
    #     yield FormRequest.from_response(response, formdata=formdata,
    #                                     callback=self.parse_login)
    #
    # def parse_login(self, response):
    #     print('>>>>>>>>'+response.text)
    #     yield from super().start_requests()
    #
    # def parse(self, response):
    #     print('>>>>>>>>'+response.text)
    #     for i in range(1, 3):
    #         time.sleep(5)
    #         item = CrawlerwebItem()
    #         name = response.css('#datu > div > ul > li:nth-child(%d) > div.datu-mingzi::text' % i).extract()
    #         cj = response.xpath('//*[@id="datu"]/div/ul/li[%d]/div[4]/text()' % i).extract()
    #         gg = response.xpath('//*[@id="datu"]/div/ul/li[%d]/div[5]/span/text()' % i).extract()
    #         xq = response.xpath('//*[@id="datu"]/div/ul/li[%d]/div[6]/span[1]/text()' % i).extract()
    #         price = response.xpath('//*[@id="datu"]/div/ul/li[%d]/div[2]/text()' % i).extract()
    #         item['name'] = name
    #         item['cj'] = cj
    #         item['gg'] = gg
    #         item['xq'] = xq
    #         item['price'] = price
    #         yield item

    # def login(self):
    #     login_url = 'https://www.hezongyy.com/auth/login'
    #     formdata = {
    #         "act": "ajax_act_login",
    #         "user_name": "test",
    #         "password": "123456",
    #         "back_act": "/index.php",
    #         "remember": "1"}
    #     yield scrapy.FormRequest(url=login_url, formdata=formdata, callback=self.parse_login)
    # def parse_login(self,response):
    #     print('>>>>>>>>' + response.text)
    #     if json.loads(response.text)["retcode"] == 20000000:
    #         print("登录成功！")
    #         # 访问主页
    #         main_url = "https://www.hezongyy.com"
    #         yield scrapy.Request(url=main_url, callback=self.parse)
    #
    #     else:
    #         print("登录失败！")

    # def parse(self, response):
    #     print('>>>>>>>>'+response.text)
        # for i in range(1, 3):
        #     time.sleep(5)
        #     item = CrawlerwebItem()
        #     name = response.css('#datu > div > ul > li:nth-child(%d) > div.datu-mingzi::text' % i).extract()
        #     cj = response.xpath('//*[@id="datu"]/div/ul/li[%d]/div[4]/text()' % i).extract()
        #     gg = response.xpath('//*[@id="datu"]/div/ul/li[%d]/div[5]/span/text()' % i).extract()
        #     xq = response.xpath('//*[@id="datu"]/div/ul/li[%d]/div[6]/span[1]' % i).extract()
        #     price = response.xpath('//*[@id="datu"]/div/ul/li[%d]/div[2]' % i).extract()
        #     item['name'] = name
        #     item['cj'] = cj
        #     item['gg'] = gg
        #     item['xq'] = xq
        #     item['price'] = price
        #     yield item

    # def parse(self, response):
    #      print(response.text)
    #      d1 = response.css('#datu > div > ul > li')
    #      for dd in d1:
    #          item = CrawlerwebItem()
    #          name = dd.css('nth-child(%d) > div.datu-mingzi::text' % dd).extract_first()
    #          cj = dd.css('nth-child(%d) > div.datu-compamy::text' % dd).extract_first()
    #          gg = dd.css('nth-child(%d) > div.datu-guige > span::text' % dd).extract()
    #          xq = dd.css('nth-child(%d) > div.datu-xiaoqi > span:nth-child(1)::text' % dd).extract()
    #          price = dd.css('nth-child(%d) > div.datu-jiage::text' % dd).extract()
    #          item['name'] = name
    #          item['compony'] = cj
    #          item['gg'] = gg
    #          item['xq'] = xq
    #          item['price'] = price
    #          yield item


# class hezongyy_py(scrapy.Spider):
#   name='hezongyy_py'
#   allowed_domains = ['hezongyy.com']
#   #1. 登录页面
#   start_urls = ['https://www.hezongyy.com/auth/login']
#   def parse(self, response):
#     #2. 代码登录
#     login_url = 'https://www.hezongyy.com/auth/login'
#     formdata={
#       "username": "测试06",
#       "pwd": "123456"
#     }
#     #3. 发送登录请求post
#     yield scrapy.FormRequest.from_response(
#       response,
#       formxpath="//*[@id='right_1']/a",
#       formdata=formdata,
#       method="POST", #覆盖之前的get请求
#       callback=self.parse_login
#     )
#
#   def parse_login(self, response):
#     #4.访问目标页面
#     member_url = "https://www.hezongyy.com/"
#     yield scrapy.Request(member_url, callback=self.parse_member)
#
#   def parse_member(self, response):
#     with open("puyao.html", 'wb') as f:
#       f.write(response.body)
#       item = CrawlerwebItem()
#       # quotes = response.xpath('//*[@id="datu"]/div/ul')
#       for i in range(1, 41):
#           name = response.css('#datu > div > ul > li:nth-child(%d) > div.datu-mingzi::text' % i).extract_first()
#           cj = response.css('#datu > div > ul > li:nth-child(%d) > div.datu-compamy::text' % i).extract_first()
#           gg = response.css('#datu > div > ul > li:nth-child(%d) > div.datu-guige > span::text' % i).extract()
#           xq = response.css('#datu > div > ul > li:nth-child(%d) > div.datu-xiaoqi > span:nth-child(1)::text' % i).extract()
#           price = response.css('#datu > div > ul > li:nth-child(%d) > div.datu-jiage::text' % i).extract()
#           item['name'] = name
#           item['compony'] = cj
#           item['gg'] = gg
#           item['xq'] = xq
#           item['price'] = price
#           yield item
#       # next = response.css('.pager .next a::attr(href)').extract_first()
#       # url = response.urljoin(next)
#       # yield scrapy.Request(url=url, callback=self.parse)


