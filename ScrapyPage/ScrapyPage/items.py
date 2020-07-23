# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerwebItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()  # 商品名称
    cj = scrapy.Field()  # 生产厂家
    gg = scrapy.Field()  # 规格
    xq = scrapy.Field()  # 效期
    sj = scrapy.Field()  # 商家
    price = scrapy.Field()  # 会员价
    price2 = scrapy.Field()  # 券后价
    price3 = scrapy.Field()

