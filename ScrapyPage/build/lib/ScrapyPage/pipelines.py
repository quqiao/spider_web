# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from twisted.enterprise import adbapi
import time

# class ScrapypagePipeline(object):
#     def process_item(self, item, spider):
#         return item

# class MysqlPipeline_Longyi_tjzq(object):
#     def __init__(self, dbpool):
#         self.dbpool = dbpool
#
#     @classmethod
#     def from_settings(cls, settings):  # 函数名固定，会被scrapy调用，直接可用settings的值
#         """
#         数据库建立连接
#         :param settings: 配置参数
#         :return: 实例化参数
#         """
#         adbparams = dict(
#             host=settings['localhost'],
#             db=settings['spider_web'],
#             username=settings['root'],
#             password=settings['123456'],
#             port=settings['3306'],
#             cursorclass=pymysql.cursors.DictCursor  # 指定cursor类型
#         )
#         # 连接数据池ConnectionPool，使用pymysql或者Mysqldb连接
#         dbpool = adbapi.ConnectionPool('pymysql', **adbparams)
#         # 返回实例化参数
#         return cls(dbpool)
#
#     def process_item(self, item, spider):
#         """
#         使用twisted将MySQL插入变成异步执行。通过连接池执行具体的sql操作，返回一个对象
#         """
#         query = self.dbpool.runInteraction(self.do_insert, item)  # 指定操作方法和操作数据
#         # 添加异常处理
#         query.addCallback(self.handle_error)  # 处理异常
#
#     def do_insert(self, cursor, item):
#         # 使用 execute() 方法执行 SQL，如果表存在则删除
#         cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#         # 对数据库进行插入操作，并不需要commit，twisted会自动commit
#         now = time.strftime("%Y-%m-%d")
#         # 使用预处理语句创建表
#         sql = """CREATE TABLE longyi_tjzq (
#                  name  CHAR(20) NOT NULL,
#                  cj  CHAR(40),
#                  gg CHAR(20),
#                  xq CHAR(20),
#                  price CHAR(20) )"""
#
#         cursor.execute(sql)
#         insert_sql = """insert into longyi_tjzq(name,cj,gg,xq,price) VALUES(%s,%s,%s,%s,%s)"""
#         cursor.execute(insert_sql, (item['name'], item['cj'], item['gg'], item['xq'],
#                                     item['price']), chartset='utf8')
#
#     def handle_error(self, failure):
#         if failure:
#             # 打印错误信息
#             print(failure)



class MysqlPipelineLongyi_tjzq(object):
    """
    同步操作
    """
    now = time.strftime("%Y-%m-%d")
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect('localhost', 'root', '123456', 'spider_web')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS longyi_tjzq_01")
        # 使用预处理语句创建表
        sql = """CREATE TABLE longyi_tjzq_01 (
                 ID    int unsigned not null  auto_increment primary key,
                 name  CHAR(20) NOT NULL,
                 cj  CHAR(40) NOT NULL,
                 gg CHAR(20) NOT NULL,
                 xq CHAR(20) NOT NULL,
                 price CHAR(20) NOT NULL )"""
        self.cursor.execute(sql)

    def process_item(self, item, spider):

        insert_sql = """insert into longyi_tjzq_01 (name,cj,gg,xq,price) VALUES(%s,%s,%s,%s,%s)
        """
        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql, (item['name'], item['cj'], item['gg'], item['xq'],
                                         item['price']))
        # 提交，不进行提交无法保存到数据库
        self.conn.commit()
        return item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()

class MysqlPipelinerjyiyao_xpsj(object):
    """
    同步操作
    """
    now = time.strftime("%Y-%m-%d")
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect('localhost', 'root', '123456', 'spider_web')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS rjyiyao_xpsj")
        # 使用预处理语句创建表
        sql = """CREATE TABLE rjyiyao_xpsj (
                 ID    int unsigned not null  auto_increment primary key,
                 name  CHAR(100) NOT NULL,
                 cj  CHAR(100) NOT NULL,
                 gg CHAR(100) NOT NULL,
                 xq CHAR(100) NOT NULL,
                 price CHAR(100) NOT NULL )"""
        self.cursor.execute(sql)

    def process_item(self, item, spider):

        insert_sql = """insert into rjyiyao_xpsj (name,cj,gg,xq,price) VALUES(%s,%s,%s,%s,%s)
        """
        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql, (item['name'], item['cj'], item['gg'], item['xq'],
                                         item['price']))
        # 提交，不进行提交无法保存到数据库
        self.conn.commit()
        return item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()

class MysqlPipelinescjrm_zszq(object):
    """
    同步操作
    """
    now = time.strftime("%Y-%m-%d")
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect('localhost', 'root', '123456', 'spider_web')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS scjrm_zszq")
        # 使用预处理语句创建表
        sql = """CREATE TABLE scjrm_zszq (
                 ID    int unsigned not null  auto_increment primary key,
                 name  CHAR(100) NOT NULL,
                 cj  CHAR(100) NOT NULL,
                 price CHAR(100) NOT NULL )"""
        self.cursor.execute(sql)

    def process_item(self, item, spider):

        insert_sql = """insert into scjrm_zszq (name,cj,price) VALUES(%s,%s,%s)
        """
        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql, (item['name'], item['cj'], item['price']))
        # 提交，不进行提交无法保存到数据库
        self.conn.commit()
        return item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()

