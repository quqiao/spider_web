# -*- coding: utf-8 -*-
"""药品终端网_阶梯价专区"""
import scrapy
import time
from ScrapyPage.items import CrawlerwebItem
from scrapy import cmdline
import time


class longyiSpider(scrapy.Spider):
    name = 'ypzdw_jtj'
    allowed_domains = ['ypzdw.com']
    start_urls = ['https://www.ypzdw.com/jshop/ca/commonRec?t=personTiered&p=1&show=all&topid=0']
    # custom_settings = {'ITEM_PIPELINES': {'ScrapyPage.pipelines.MysqlPipelineLongyi_tjzq': 300,}}

    def start_requests(self):
        for i in range(1, 183):
            zszq = "https://www.ypzdw.com/jshop/ca/commonRec?t=personTiered&p=%d&show=all&topid=0" % i
            yield scrapy.Request(url=zszq, callback=self.parse)

    def parse(self, response):
        # print(response.text)
        time.sleep(1)
        for i in range(1, 21):
            item = CrawlerwebItem()
            name = response.xpath('/html/body/div[2]/div[2]/div[2]/div/ul/li[%d]/div[2]/a/text()' % i).extract()
            cj = response.xpath('/html/body/div[2]/div[2]/div[2]/div/ul/li[%d]/div[3]/p[2]/text()' % i).extract()
            gg = response.xpath('/html/body/div[2]/div[2]/div[2]/div/ul/li[%d]/div[3]/p[1]/text()' % i).extract()
            sj = response.xpath('/html/body/div[2]/div[2]/div[2]/div/ul/li[%d]/div[3]/p[3]/a/text()' % i).extract()
            price = response.xpath('/html/body/div[2]/div[2]/div[2]/div/ul/li[%d]/div[1]/a/div[4]/p[2]/text()' % i).extract()
            # price2 = response.xpath('/html/body/div[4]/div/div[4]/ul/li[%d]/p[8]/span[2]/text()' % i).extract()
            item['name'] = name
            item['cj'] = cj
            item['gg'] = gg
            item['sj'] = sj
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

