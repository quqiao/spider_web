from django.http import HttpResponse
from spider_page.models import Test

def slec_all(request):
    """取出User表里面user_name 、psw 、mail全部数据"""
    users = ""
    psws = ""
    mails = ""
    ret = Test.objects.all()

    # 返回queryset对象，可迭代
    for i in ret:
        users += " " + i.user_name  # 获取user_name字段
        psws += " " + i.psw  # 获取psw字段
        mails += " " + i.mail  # 获取mail字段

    return HttpResponse('''<p>查询user结果：%s</p>
                            <p>查询psw结果：%s</p>
                            <p>查询psw结果：%s</p>''' % (users, psws, mails))