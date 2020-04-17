import scrapy


class RenrenLoginSpider(scrapy.Spider):
    name = 'renren_login'
    allowed_domains = ['www.renren.com/']
    start_urls = ['http://www.renren.com/']

    # def parse(self, response):
    def start_requests(self):
        # url 来自于 <form method="post" id="loginForm" class="login-form" action="http://www.renren.com/PLogin.do">
        # 中的 action
        url = 'http://www.renren.com/PLogin.do'
        # data 的 key 来自于登录成功的跳转页，值为账号和密码
        data = {
            'email': '***',
            'password': '***'
        }
        # scrapy.FormRequest() 用于提交 form 表单，post，用于登录
        request = scrapy.FormRequest(url, formdata=data, callback=self.parse_page)
        yield request

    def parse_page(self, response):
        # 为了验证登陆成功，查看别人的人人主页
        request = scrapy.Request(url='http://www.renren.com/464562352/profile', callback=self.parse_profile, dont_filter=True)
        yield request

    def parse_profile(self, response):
        with open('jing.html','w',encoding='utf8') as fp:
            fp.write(response.text)
