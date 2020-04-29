# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import requests
import pytesseract
from PIL import Image, ImageEnhance


class ScrapypageSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ScrapypageDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class Login_page(object):
    # type()元类，object 基类
    def process_request(self,  request, spider):
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 使用无头谷歌浏览器模式
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        '''
        :param request: 请求
        :param spider: 爬虫名
        :return:
        '''
        # 判断是哪个爬虫
        if spider.name == 'scjrm_zszq':
            # 判断是否是登陆
            if request.url == "http://www.scjrm.com/zs/index.html?page=1":
                spider.driver = webdriver.Chrome(
                    executable_path="C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe")
                # if request.url == "http://www.scjrm.com/zs/index.html?page=1":
                spider.driver.get("http://www.scjrm.com/site/login.html")
                # spider.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/h3/a').click()
                time.sleep(2)
                #模拟输入账号密码
                username = spider.driver.find_element_by_id('phonenumber')
                password = spider.driver.find_element_by_id('password')
                username.send_keys('18030535053')
                password.send_keys('123456')
                #模拟点击“登录”按钮
                spider.driver.find_element_by_id('sub_bt').click()
                time.sleep(1)
                spider.driver.get(request.url)
                time.sleep(3)
                spider.cookies = spider.driver.get_cookies()
                time.sleep(1)
                return HtmlResponse(url=spider.driver.current_url,  # 登录后的url
                                    body=spider.driver.page_source,  # html源码
                                    encoding='utf-8')

            # 不是登录
            else:
                spider.driver.get(request.url)
                return HtmlResponse(url=spider.driver.current_url,  # 当前连接
                                    body=spider.driver.page_source,  # 源代码  # 源代码
                                    encoding="utf-8", request=request)  # 返回页面信息

        # if spider.name == 'scjuchuang_yxzq':
        #     # 判断是否是登陆
        #     # if request.url.find('login') != -1:
        #     spider.driver = webdriver.Chrome(executable_path="C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe", chrome_options=chrome_options)
        #     spider.driver.get('https://www.scjuchuang.com/login')
        #     # spider.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/h3/a').click()
        #     time.sleep(2)
        #     #模拟输入账号密码
        #     username = spider.driver.find_element_by_class_name('loginName')
        #     password = spider.driver.find_element_by_class_name('loginPassword')
        #     username.send_keys('yczs123')
        #     password.send_keys('123456')
        #     #模拟点击“登录”按钮
        #     spider.driver.find_element_by_class_name('loginBtn').click()
        #     time.sleep(1)
        #     spider.driver.get('https://www.scjuchuang.com/goods?attr=1&page=1')
        #     # spider.driver.find_element_by_link_text('院线专区').click()
        #     spider.cookies = spider.driver.get_cookies()
        #     return HtmlResponse(url=spider.driver.current_url,  # 登录后的url
        #                         body=spider.driver.page_source,  # html源码
        #                         encoding='utf-8')

        elif spider.name == 'rjyiyao_xpsj':
            # 判断是否是登陆
            if request.url == 'http://new.rjyiyao.com/web/product/group/5?page=1':
            # if request.url.find('login') != -1:
                spider.driver = webdriver.Chrome(executable_path="C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe")
                spider.driver.get('http://new.rjyiyao.com/web/login')
                # spider.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/h3/a').click()
                time.sleep(2)
                #模拟输入账号密码
                username = spider.driver.find_element_by_id('username')
                password = spider.driver.find_element_by_id('password')
                username.send_keys('18030535053')
                password.send_keys('123456')
                #模拟点击“登录”按钮
                spider.driver.find_element_by_id('btnLogin').click()
                time.sleep(1)
                # spider.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[3]/div[2]/a[2]/img').click()  # 新品上架
                # windows = spider.driver.window_handles
                # spider.driver.switch_to.window(windows[1])  # 切换到第二页
                spider.driver.get('http://new.rjyiyao.com/web/product/group/5?page=1')
                time.sleep(5)
                spider.cookies = spider.driver.get_cookies()
                return HtmlResponse(url=spider.driver.current_url,  # 登录后的url
                                    body=spider.driver.page_source,  # html源码
                                    encoding='utf-8')
            else:
                spider.driver.get(request.url)
                time.sleep(5)
                return HtmlResponse(url=spider.driver.current_url,  # 当前连接
                                    body=spider.driver.page_source,  # 源代码  # 源代码
                                    encoding="utf-8", request=request)  # 返回页面信息

        if spider.name == 'rjyiyao_zkzq':
            # 判断是否是登陆
            # if request.url.find('login') != -1:
            if request.url == "http://new.rjyiyao.com/web/product/sale/3?page=1":
                spider.driver = webdriver.Chrome(executable_path="C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe")
                spider.driver.get('http://new.rjyiyao.com/web/login')
                # spider.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/h3/a').click()
                time.sleep(1)
                #模拟输入账号密码
                username = spider.driver.find_element_by_id('username')
                password = spider.driver.find_element_by_id('password')
                username.send_keys('18030535053')
                password.send_keys('123456')
                #模拟点击“登录”按钮
                spider.driver.find_element_by_id('btnLogin').click()
                time.sleep(2)
                spider.driver.get(request.url)
                # spider.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[3]/div[2]/a[2]/img').click()  # 新品上架
                # windows = spider.driver.window_handles
                # spider.driver.switch_to.window(windows[1])  # 切换到第二页
                time.sleep(5)
                spider.cookies = spider.driver.get_cookies()
                return HtmlResponse(url=spider.driver.current_url,  # 登录后的url
                                    body=spider.driver.page_source,  # html源码
                                    encoding='utf-8')
            else:
                spider.driver.get(request.url)
                time.sleep(5)
                return HtmlResponse(url=spider.driver.current_url,  # 当前连接
                                    body=spider.driver.page_source,  # 源代码  # 源代码
                                    encoding="utf-8", request=request)  # 返回页面信息

        elif spider.name == 'sckxyy_ypzq':
            # 判断是否是登陆
            # if request.url.find('login') != -1:
            if request.url == 'http://www.sckxyy.com/Login.html':
                spider.driver = webdriver.Chrome(executable_path="C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe")
                spider.driver.get('http://www.sckxyy.com/Login.html')
                time.sleep(2)
                #模拟输入账号密码
                username = spider.driver.find_element_by_id('usernameLogin')
                password = spider.driver.find_element_by_id('passwordLogin')
                username.send_keys('bianyuantianshi')
                password.send_keys('123456')
                #模拟点击“登录”按钮
                spider.driver.find_element_by_id('userLogin').click()
                time.sleep(1)
                # spider.cookies = spider.driver.get_cookies()
                spider.driver.get('http://www.sckxyy.com/Drug_zone.html')
                return HtmlResponse(url=spider.driver.current_url,  # 登录后的url
                                    body=spider.driver.page_source,  # html源码
                                    encoding='utf-8')
            else:
                for i in range(10):
                    time.sleep(2)
                    js_bottom1 = "var q=document.documentElement.scrollTop=10000"
                    spider.driver.execute_script(js_bottom1)
                    time.sleep(1)
                    spider.driver.find_element_by_class_name("next").click()
                    return HtmlResponse(url=spider.driver.current_url,  # 登录后的url
                                    body=spider.driver.page_source,  # html源码
                                    encoding='utf-8', request=request)

        elif spider.name == 'ysbang_zxxd':
            spider.driver = webdriver.Chrome(executable_path="C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe")
            spider.driver.get('https://dian.ysbang.cn/index.html#/login')
            spider.driver.implicitly_wait(10)
            spider.driver.maximize_window()
            userElement = spider.driver.find_element_by_id("userAccount")  # 用户名元素
            passElement = spider.driver.find_element_by_id("password")  # 密码元素
            codeElement = spider.driver.find_element_by_id("captcha")  # 验证码输入框
            imgElement = spider.driver.find_element_by_id("captchaImg")  # 验证图片元素
            # 2、截取屏幕内容，保存到本地
            spider.driver.save_screenshot("F://django/spider_web/ScrapyPage/ScrapyPage/yzm/01.png")

            # 3、打开截图，获取验证码位置，截取保存验证码
            ran = Image.open("F://django/spider_web/ScrapyPage/ScrapyPage/yzm/01.png")
            box = (1252, 394, 1511, 433)  # 获取验证码位置,自动定位不是很明白，就使用了手动定位，代表（左，上，右，下）
            ran.crop(box).save("F://django/spider_web/ScrapyPage/ScrapyPage/yzm/02.png")

            # 4、获取验证码图片，读取验证码
            imageCode = Image.open("F://django/spider_web/ScrapyPage/ScrapyPage/yzm/02.png")  # 图像增强，二值化
            # imageCode.load()
            sharp_img = ImageEnhance.Contrast(imageCode).enhance(2.0)
            sharp_img.save("F://django/spider_web/ScrapyPage/ScrapyPage/yzm/03.png")
            sharp_img.load()  # 对比度增强
            time.sleep(2)
            print(sharp_img)
            code = pytesseract.image_to_string(sharp_img).strip()
            # 5、收到验证码，进行输入验证
            print("<<<<<<<<哈哈哈" + code)
            userElement.send_keys('admin')
            passElement.send_keys('admin123')
            # time.sleep(3)
            codeElement.send_keys(code)
            click_login = spider.driver.find_element_by_id("loginBtn")
            click_login.click()
            time.sleep(5)




