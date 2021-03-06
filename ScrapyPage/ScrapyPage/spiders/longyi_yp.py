# -*- coding: utf-8 -*-
"""龙一医药网_药品专区"""
import scrapy
import time
from ScrapyPage.items import CrawlerwebItem
from scrapy import cmdline
import time


class longyiSpider(scrapy.Spider):
    name = 'longyi_yp'
    allowed_domains = ['longyiyy.com']
    start_urls = ['http://www.longyiyy.com/goods-filter-0-0-0-0-0-0-1-1.html"']
    # custom_settings = {'ITEM_PIPELINES': {'ScrapyPage.pipelines.MysqlPipelineLongyi_tjzq': 300,}}

    def start_requests(self):
        for i in range(1, 404):
            zszq = "http://www.longyiyy.com/goods-filter-0-0-0-0-0-0-1-%d.html" % i
            yield scrapy.Request(url=zszq, callback=self.parse)

    def parse(self, response):
        # print(response.text)
        time.sleep(1)
        for i in range(1, 21):
            item = CrawlerwebItem()
            name = response.xpath('//*[@id="pro_list1"]/li[%d]/p[1]/a/text()' % i).extract()
            cj = response.xpath('//*[@id="pro_list1"]/li[%d]/p[3]/text()' % i).extract()
            gg = response.xpath('//*[@id="pro_list1"]/li[%d]/p[4]/span/text()' % i).extract()
            xq = response.xpath('//*[@id="pro_list1"]/li[%d]/p[6]/span[1]/i/text()' % i).extract()
            price = response.xpath('//*[@id="pro_list1"]/li[%d]/p[2]/span[2]/text()' % i).extract()
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

