# -*- coding: utf-8 -*-
"""龙一医药网_特价专区"""
import scrapy
import time
from ScrapyPage.items import CrawlerwebItem
from scrapy import cmdline
import time


class longyiSpider(scrapy.Spider):
    name = 'longyi_tjzq'
    allowed_domains = ['longyiyy.com']
    start_urls = ['http://www.longyiyy.com/events-547.html']
    custom_settings = {'ITEM_PIPELINES': {'ScrapyPage.pipelines.MysqlPipelineLongyi_tjzq': 300,}}


    # def parse(self, response):
    # def start_requests(self):
    #     # url 来自于 <form method="post" id="loginForm" class="login-form" action="">
    #     # 中的 action
    #     url = 'http://www.longyiyy.com/login.html'
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
    #     # 为了验证登陆成功，查看药品专区主页
    #     time.sleep(1)
    #     request = scrapy.Request(url='http://www.longyiyy.com/events-542.html', callback=self.parse, dont_filter=True)
    #     yield request

    def start_requests(self):
        for i in range(1, 10):
            zszq = "http://www.longyiyy.com/events-filter-547-%d-3.html" % i
            yield scrapy.Request(url=zszq, callback=self.parse)

    def parse(self, response):
        # print(response.text)
        time.sleep(1)
        for i in range(1, 41):
            time.sleep(1)
            item = CrawlerwebItem()
            name = response.xpath('/html/body/div[4]/div/div[4]/ul/li[%d]/p[1]/a/text()' % i).extract()
            cj = response.xpath('/html/body/div[4]/div/div[4]/ul/li[%d]/p[2]/text()' % i).extract()
            gg = response.xpath('/html/body/div[4]/div/div[4]/ul/li[%d]/p[3]/span/text()' % i).extract()
            xq = response.xpath('/html/body/div[4]/div/div[4]/ul/li[%d]/p[6]/text()' % i).extract()
            price = response.xpath('/html/body/div[4]/div/div[4]/ul/li[%d]/p[7]/span[1]/text()' % i).extract()
            # price2 = response.xpath('/html/body/div[4]/div/div[4]/ul/li[%d]/p[8]/span[2]/text()' % i).extract()
            item['name'] = name
            item['cj'] = cj
            item['gg'] = gg
            item['xq'] = xq
            item['price'] = price
            # item['price2'] = price2
            yield item
        # next_page = response.xpath("//*[text()='下一页']/@href").extract_first()
        # if next_page is not None:
        #     next_page1 = response.urljoin(next_page)
        #     yield scrapy.Request(next_page1, callback=self.parse)

    # # 方式一：注意execute的参数类型为一个列表
    # cmdline.execute('scrapy crawl spidername'.split())
    # # 方式二:注意execute的参数类型为一个列表
    # cmdline.execute(['scrapy', 'crawl', 'spidername'])
    # 方式三：execute执行本脚本
    # now = time.strftime("%Y-%m-%d")
    # cmdline.execute('scrapy crawl longyi_tjzq -o longyi_tjzq_%s -s FEED_EXPORT_ENCODING=UTF-8' % now)

