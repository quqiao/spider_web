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
class MysqlPipelinehezongyy_py(object):
    """合纵药易购_普药专区"""
    now = time.strftime("%Y-%m-%d")
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect('localhost', 'root', '123456', 'spider_web')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS hezongyy_py")
        # 使用预处理语句创建表
        sql = """
              CREATE TABLE hezongyy_py (
                 ID int unsigned auto_increment primary key,
                 name VARCHAR(100),
                 cj VARCHAR(100),
                 gg VARCHAR(100),
                 xq VARCHAR(100),
                 price VARCHAR(100),
                 price2 VARCHAR(100) DEFAULT 'Shanghai',
                 price3 VARCHAR(100))
              """
        self.cursor.execute(sql)

    def process_item(self, item, spider):

        insert_sql = """
                     insert into hezongyy_py 
                     (name,cj,gg,xq,price,price2) 
                     VALUES
                     (%s,%s,%s,%s,%s,%s)
                     """
        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql, (item['name'], item['cj'], item['gg'], str(item['xq']), item['price'], str(item['price2'])))
        # 提交，不进行提交无法保存到数据库
        self.conn.commit()
        return item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()


class MysqlPipelineLongyi_tjzq(object):
    """龙一医药网_特价专区"""
    now = time.strftime("%Y-%m-%d")
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect('localhost', 'root', '123456', 'spider_web')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS longyi_tjzq")
        # 使用预处理语句创建表
        sql = """
              CREATE TABLE longyi_tjzq(
                 ID    int unsigned NOT NULL auto_increment primary key,
                 name  VARCHAR(100),
                 cj  VARCHAR(100),
                 gg VARCHAR(100),
                 xq VARCHAR(100),
                 price VARCHAR(100),
                 price2 VARCHAR(100),
                 price3 VARCHAR(100))
              """
        self.cursor.execute(sql)

    def process_item(self, item, spider):

        insert_sql = """
                     insert into longyi_tjzq
                     (name,cj,gg,xq,price) 
                     VALUES
                     (%s,%s,%s,%s,%s)
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

class MysqlPipelineLongyi_yp(object):
    """龙一医药网_药品专区"""
    now = time.strftime("%Y-%m-%d")
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect('localhost', 'root', '123456', 'spider_web')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS longyi_yp")
        # 使用预处理语句创建表
        sql = """
              CREATE TABLE longyi_yp(
                 ID    int unsigned NOT NULL  auto_increment primary key,
                 name  VARCHAR(100),
                 cj  VARCHAR(100),
                 gg VARCHAR(100),
                 xq VARCHAR(100),
                 price VARCHAR(100),
                 price2 VARCHAR(100),
                 price3 VARCHAR(100))
              """
        self.cursor.execute(sql)

    def process_item(self, item, spider):

        insert_sql = """
                     insert into longyi_yp
                     (name,cj,gg,xq,price) 
                     VALUES
                     (%s,%s,%s,%s,%s)
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
    """蓉锦医药网_新品上架"""
    now = time.strftime("%Y-%m-%d")
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect('localhost', 'root', '123456', 'spider_web')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS rjyiyao_xpsj")
        # 使用预处理语句创建表
        sql = """CREATE TABLE rjyiyao_xpsj (
                 ID    int unsigned NOT NULL  auto_increment primary key,
                 name  VARCHAR(100),
                 cj  VARCHAR(100),
                 gg VARCHAR(100),
                 xq VARCHAR(100),
                 price VARCHAR(100),
                 price2 VARCHAR(100),
                 price3 VARCHAR(100))"""
        self.cursor.execute(sql)

    def process_item(self, item, spider):

        insert_sql = """insert into rjyiyao_xpsj (name,cj,gg,xq,price) VALUES(%s,%s,%s,%s,%s)"""
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

class MysqlPipelinerjyiyao_zkzq(object):
    """蓉锦医药网_折扣专区"""
    now = time.strftime("%Y-%m-%d")
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect('localhost', 'root', '123456', 'spider_web')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS rjyiyao_zkzq")
        # 使用预处理语句创建表
        sql = """CREATE TABLE rjyiyao_zkzq (
                 ID    int unsigned NOT NULL  auto_increment primary key,
                 name  VARCHAR(100),
                 cj  VARCHAR(100),
                 gg VARCHAR(100),
                 xq VARCHAR(100),
                 price VARCHAR(100),
                 price2 VARCHAR(100),
                 price3 VARCHAR(100))"""
        self.cursor.execute(sql)

    def process_item(self, item, spider):

        insert_sql = """insert into rjyiyao_zkzq (name,cj,gg,xq,price) VALUES(%s,%s,%s,%s,%s)
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
    """四川金仁药淘齐_诊所专区"""
    now = time.strftime("%Y-%m-%d")
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect('localhost', 'root', '123456', 'spider_web')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS scjrm_zszq")
        # 使用预处理语句创建表
        sql = """
                 CREATE TABLE scjrm_zszq (
                 ID    int unsigned NOT NULL  auto_increment primary key,
                 name  VARCHAR(100),
                 cj  VARCHAR(100),
                 xq  VARCHAR(100),
                 gg  VARCHAR(100),
                 price VARCHAR(100),
                 price2 VARCHAR(100),
                 price3 VARCHAR(100))
              """
        self.cursor.execute(sql)

    def process_item(self, item, spider):
        insert_sql = """insert into scjrm_zszq (name,cj,price) VALUES(%s,%s,%s)"""
        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql, (item['name'], item['cj'], item['price']))
        # 提交，不进行提交无法保存到数据库
        self.conn.commit()
        return item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()

class MysqlPipelinescjuchuang_py(object):
    """聚创医药网_院线专区"""
    now = time.strftime("%Y-%m-%d")
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect('localhost', 'root', '123456', 'spider_web')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS scjuchuang_py")
        # 使用预处理语句创建表
        sql = """
                 CREATE TABLE scjuchuang_py (
                 ID    int unsigned NOT NULL  auto_increment primary key,
                 name  VARCHAR(100),
                 cj  VARCHAR(100),
                 gg VARCHAR(100),
                 xq VARCHAR(100),
                 price VARCHAR(100),
                 price2 VARCHAR(100),
                 price3 VARCHAR(100))
              """
        self.cursor.execute(sql)

    def process_item(self, item, spider):
        insert_sql = """insert into scjuchuang_py (name,cj,gg,xq,price,price2,price3) VALUES(%s,%s,%s,%s,%s,%s,%s)"""
        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql, (item['name'], item['cj'], item['gg'], item['xq'], str(item['price']), str(item['price2']), str(item['price3'])))
        # 提交，不进行提交无法保存到数据库
        self.conn.commit()
        return item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()

class MysqlPipelinescjuchuang_tjzq(object):
    """聚创医药网_院线专区"""
    now = time.strftime("%Y-%m-%d")
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect('localhost', 'root', '123456', 'spider_web')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS scjuchuang_tjzq")
        # 使用预处理语句创建表
        sql = """
                 CREATE TABLE scjuchuang_tjzq (
                 ID    int unsigned NOT NULL  auto_increment primary key,
                 name  VARCHAR(100),
                 cj  VARCHAR(100),
                 gg VARCHAR(100),
                 xq VARCHAR(100),
                 price VARCHAR(100),
                 price2 VARCHAR(100),
                 price3 VARCHAR(100))
              """
        self.cursor.execute(sql)

    def process_item(self, item, spider):
        insert_sql = """insert into scjuchuang_tjzq (name,cj,gg,xq,price) VALUES(%s,%s,%s,%s,%s)"""
        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql, (str(item['name']), str(item['cj']), str(item['gg']), str(item['xq']), str(item['price'])))
        # 提交，不进行提交无法保存到数据库
        self.conn.commit()
        return item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()

class MysqlPipelinescjuchuang_yxzq(object):
    """聚创医药网_院线专区"""
    now = time.strftime("%Y-%m-%d")
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect('localhost', 'root', '123456', 'spider_web')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS scjuchuang_yxzq")
        # 使用预处理语句创建表
        sql = """
                 CREATE TABLE scjuchuang_yxzq (
                 ID    int unsigned NOT NULL  auto_increment primary key,
                 name  VARCHAR(100),
                 cj  VARCHAR(100),
                 gg VARCHAR(100),
                 xq VARCHAR(100),
                 price VARCHAR(100),
                 price2 VARCHAR(100),
                 price3 VARCHAR(100))
              """
        self.cursor.execute(sql)

    def process_item(self, item, spider):
        insert_sql = """insert into scjuchuang_yxzq (name,cj,gg,xq,price) VALUES(%s,%s,%s,%s,%s)"""
        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql, (item['name'], item['cj'], item['gg'], item['xq'], item['price']))
        # 提交，不进行提交无法保存到数据库
        self.conn.commit()
        return item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()


class MysqlPipelinesckxyy_ypzq(object):
    """科欣医药网_药品专区"""
    now = time.strftime("%Y-%m-%d")
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect('localhost', 'root', '123456', 'spider_web')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS sckxyy_ypzq")
        # 使用预处理语句创建表
        sql = """CREATE TABLE sckxyy_ypzq (
                 ID    int unsigned NOT NULL  auto_increment primary key,
                 name  VARCHAR(100),
                 cj  VARCHAR(100),
                 gg VARCHAR(100),
                 xq VARCHAR(100),
                 price VARCHAR(100),
                 price2 VARCHAR(100),
                 price3 VARCHAR(100))"""
        self.cursor.execute(sql)

    def process_item(self, item, spider):
        insert_sql = """insert into sckxyy_ypzq (name,cj,gg,xq,price) VALUES(%s,%s,%s,%s,%s)"""
        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql, (item['name'], item['cj'], item['gg'], item['xq'], item['price']))
        # 提交，不进行提交无法保存到数据库
        self.conn.commit()
        return item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()

class MysqlPipelinescytyy_tjzq(object):
    """粤通医药网_诊所专区"""
    now = time.strftime("%Y-%m-%d")
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect('localhost', 'root', '123456', 'spider_web')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS scytyy_tjzq")
        # 使用预处理语句创建表
        sql = """CREATE TABLE scytyy_tjzq (
                 ID    int unsigned NOT NULL  auto_increment primary key,
                 name  VARCHAR(100),
                 cj  VARCHAR(100),
                 gg VARCHAR(100),
                 xq VARCHAR(100),
                 price VARCHAR(100),
                 price2 VARCHAR(100),
                 price3 VARCHAR(100))"""
        self.cursor.execute(sql)

    def process_item(self, item, spider):
        insert_sql = """insert into scytyy_tjzq(name,cj,gg,xq,price) VALUES(%s,%s,%s,%s,%s)"""
        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql, (item['name'], item['cj'], item['gg'], item['xq'], item['price']))
        # 提交，不进行提交无法保存到数据库
        self.conn.commit()
        return item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()

class MysqlPipelinescytyy_zszq(object):
    """粤通医药网_诊所专区"""
    now = time.strftime("%Y-%m-%d")
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect('localhost', 'root', '123456', 'spider_web')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS scytyy_zszq")
        # 使用预处理语句创建表
        sql = """CREATE TABLE scytyy_zszq (
                 ID    int unsigned NOT NULL  auto_increment primary key,
                 name  VARCHAR(100),
                 cj  VARCHAR(100),
                 gg VARCHAR(100),
                 xq VARCHAR(100),
                 price VARCHAR(100),
                 price2 VARCHAR(100),
                 price3 VARCHAR(100))"""
        self.cursor.execute(sql)

    def process_item(self, item, spider):
        insert_sql = """insert into scytyy_zszq (name,cj,gg,xq,price) VALUES(%s,%s,%s,%s,%s)"""
        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql, (item['name'], item['cj'], item['gg'], item['xq'], item['price']))
        # 提交，不进行提交无法保存到数据库
        self.conn.commit()
        return item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()


class MysqlPipelineysbang_zxxd(object):
    """粤通医药网_诊所专区"""
    now = time.strftime("%Y-%m-%d")
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect('localhost', 'root', '123456', 'spider_web')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS ysbang_zxxd")
        # 使用预处理语句创建表
        sql = """CREATE TABLE ysbang_zxxd (
                 ID    int unsigned NOT NULL  auto_increment primary key,
                 name  VARCHAR(100) NOT NULL,
                 cj  VARCHAR(100) NOT NULL,
                 xq  VARCHAR(100) NOT NULL,
                 gg VARCHAR(100) NOT NULL,
                 price VARCHAR(100) NOT NULL,
                 price2 VARCHAR(100) NOT NULL,
                 price3 VARCHAR(100) NOT NULL)"""
        self.cursor.execute(sql)

    def process_item(self, item, spider):
        insert_sql = """insert into ysbang_zxxd (name,cj,xq,price) VALUES(%s,%s,%s,%s)"""
        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql, (item['name'], item['cj'], item['xq'], item['price']))
        # 提交，不进行提交无法保存到数据库
        self.conn.commit()
        return item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()