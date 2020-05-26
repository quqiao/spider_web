from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, reverse
import requests
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from spider_page.models import longyitjzq, rjyiyaoxpsj, rjyiyaozkzq, \
                               scjrmzszq, scjuchuangyxzq, sckxyyypzq, scytyyzszq, \
                                ysbangzxxd,hezongyypy,scjuchuangtjzq,scjuchuangpy, longyiyp,scytyytjzq,User,scjuchuangjtj
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'index.html')  #, locals()

"""合纵药易购——普药专区"""
def start_hezongyy_py(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'hezongyy_py'}
        startjob = requests.post(url=url, data=data).text
        global jobid1
        jobid1 = eval(startjob)["jobid"]
        url2 = 'http://127.0.0.1:6800/listjobs.json?project=ScrapyPage'
        listjobs = requests.get(url=url2).text
        print(listjobs)
        listjobs1 = eval(listjobs)["running"]
        print(listjobs1)
        list1 = []
        for i in range(len(listjobs1)):
            list1.append(listjobs1[i]["id"])
        if jobid1 in list1:
            return JsonResponse({'result': '爬虫启动成功'}, json_dumps_params={'ensure_ascii': False})
        else:
            return JsonResponse({'result': '爬虫启动失败'}, json_dumps_params={'ensure_ascii': False})

def hezongyy_py(request):
    try:
        # url2 = 'http://127.0.0.1:6800/listjobs.json?project=ScrapyPage'
        # listjobs = requests.get(url=url2).text
        # print(listjobs)
        # listjobs1 = eval(listjobs)["running"]
        # print(listjobs1)
        # list1 = []
        # for i in range(len(listjobs1)):
        #     list1.append(listjobs1[i]["id"])
        # listjobs2 = eval(listjobs)["finished"]
        # print(listjobs2)
        # list2 = []
        # for i in range(len(listjobs2)):
        #     list2.append(listjobs2[i]["id"])
        # if jobid in list1:
        #     return JsonResponse({'result': '正在爬取中，请不要重复操作'}, json_dumps_params={'ensure_ascii':False})
        # if jobid in list2:
        #     users = hezongyypy.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
        #     return render(request, 'hezongyy_py.html', {'users': users})
        url3 ="http://localhost:6800/logs/ScrapyPage/hezongyy_py/%s.log" % jobid1
        res = requests.request(method="get", url=url3)
        res1 = res.text
        if "Spider closed" in res1:
            users = hezongyypy.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
            return render(request, 'hezongyy_py.html', {'users': users})
        else:
            return JsonResponse({'result': '正在爬取中，请不要重复操作'}, json_dumps_params={'ensure_ascii': False})

    except NameError:
        return JsonResponse({'result': '爬虫还未启动'}, json_dumps_params={'ensure_ascii':False})
    except:
        return JsonResponse({'result': '爬虫服务器还未启动，请联系管理员'}, json_dumps_params={'ensure_ascii':False})

"""龙一医药网——特价专区"""
def start_longyi_tjzq(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'longyi_tjzq'}
        startjob = requests.post(url=url, data=data).text
        global jobid2
        jobid2 = eval(startjob)["jobid"]
        url2 = 'http://127.0.0.1:6800/listjobs.json?project=ScrapyPage'
        listjobs = requests.get(url=url2).text
        print(listjobs)
        listjobs1 = eval(listjobs)["running"]
        print(listjobs1)
        list1 = []
        for i in range(len(listjobs1)):
            list1.append(listjobs1[i]["id"])
        if jobid2 in list1:
            return JsonResponse({'result': '爬虫启动成功,获取jobid成功'}, json_dumps_params={'ensure_ascii': False})
        else:
            return JsonResponse({'result': '爬虫启动成功，获取jobid失败'}, json_dumps_params={'ensure_ascii': False})

def longyi_tjzq(request):
    try:
        url3 = "http://localhost:6800/logs/ScrapyPage/longyi_tjzq/%s.log" % jobid2
        res = requests.request(method="get", url=url3)
        res1 = res.text
        if "Spider closed" in res1:
            users = hezongyypy.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
            return render(request, 'hezongyy_py.html', {'users': users})
        else:
            return JsonResponse({'result': '正在爬取中，请不要重复操作'}, json_dumps_params={'ensure_ascii': False})

    except NameError:
        return JsonResponse({'result': '爬虫还未启动'}, json_dumps_params={'ensure_ascii': False})
    except:
        return JsonResponse({'result': '爬虫服务器还未启动，请联系管理员'}, json_dumps_params={'ensure_ascii': False})

"""龙一医药网——药品专区"""
def start_longyi_yp(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'longyi_yp'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})

def longyi_yp(request):
    users = longyiyp.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'longyi_yp.html', {'users': users})


"""蓉锦医药网——新品上架"""
def start_rjyiyao_xpsj(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'rjyiyao_xpsj'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})
def rjyiyao_xpsj(request):
    users = rjyiyaoxpsj.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'rjyiyao_xpsj.html', {'users': users})

"""蓉锦医药网——折扣专区"""
def start_rjyiyao_zkzq(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'rjyiyao_zkzq'}
        startjob = requests.post(url=url, data=data).text
        global jobid5
        jobid5 = eval(startjob)["jobid"]
        url2 = 'http://127.0.0.1:6800/listjobs.json?project=ScrapyPage'
        listjobs = requests.get(url=url2).text
        print(listjobs)
        listjobs1 = eval(listjobs)["running"]
        print(listjobs1)
        list1 = []
        for i in range(len(listjobs1)):
            list1.append(listjobs1[i]["id"])
        if jobid5 in list1:
            return JsonResponse({'result': '爬虫启动成功,获取jobid成功'}, json_dumps_params={'ensure_ascii': False})
        else:
            return JsonResponse({'result': '爬虫启动成功，获取jobid失败'}, json_dumps_params={'ensure_ascii': False})
def rjyiyao_zkzq(request):
    try:
        users = rjyiyaozkzq.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
        url3 = "http://localhost:6800/logs/ScrapyPage/rjyiyao_zkzq/%s.log" % jobid5
        res = requests.request(method="get", url=url3)
        res1 = res.text
        if "Spider closed" in res1:
            users = hezongyypy.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
            return render(request, 'hezongyy_py.html', {'users': users})
        else:
            return JsonResponse({'result': '正在爬取中，请不要重复操作'}, json_dumps_params={'ensure_ascii': False})
    except NameError:
        return JsonResponse({'result': '爬虫还未启动'}, json_dumps_params={'ensure_ascii': False})
    except:
        return JsonResponse({'result': '爬虫服务器还未启动，请联系管理员'}, json_dumps_params={'ensure_ascii': False})

"""四川金仁药淘齐——诊所专区"""
def scjrm_zszq(request):
    users = scjrmzszq.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'scjrm_zszq.html', {'users': users})
def start_scjrm_zszq(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'scjrm_zszq'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})

"""四川聚创医药网——阶梯价"""
def scjuchuang_jtj(request):
    users = scjuchuangjtj.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'scjuchuang_jtj.html', {'users': users})
def start_scjuchuang_jtj(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'scjuchuang_jtj'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})

"""四川聚创医药网——普药专区"""
def scjuchuang_py(request):
    users = scjuchuangpy.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'scjuchuang_py.html', {'users': users})
def start_scjuchuang_py(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'scjuchuang_py'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})

"""四川聚创医药网——特价专区"""
def scjuchuang_tjzq(request):
    users = scjuchuangtjzq.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'scjuchuang_tjzq.html', {'users': users})
def start_scjuchuang_tjzq(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'scjuchuang_tjzq'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})

"""四川聚创医药网——院线专区"""
def scjuchuang_yxzq(request):
    users = scjuchuangyxzq.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'scjuchuang_yxzq.html', {'users': users})
def start_scjuchuang_yxzq(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'scjuchuang_yxzq'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})

"""四川科欣医药——药品专区"""
def sckxyy_ypzq(request):
    users = sckxyyypzq.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'sckxyy_ypzq.html', {'users': users})
def start_sckxyy_ypzq(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'sckxyy_ypzq'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})

"""粤通医药网——特价专区"""
def scytyy_tjzq(request):
    users = scytyytjzq.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'scytyy_tjzq.html', {'users': users})
def start_scytyy_tjzq(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'scytyy_tjzq'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})

"""粤通医药网——诊所专区"""
def scytyy_zszq(request):
    users = scytyyzszq.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'scytyy_zszq.html', {'users': users})
def start_scytyy_zszq(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'scytyy_zszq'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})

"""药师帮——在线下单"""
def ysbang_zxxd(request):
    users = ysbangzxxd.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'ysbang_zxxd.html', {'users': users})
def start_ysbang_zxxd(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'ysbang_zxxd'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})


def test_demo(request):
    context = {'name': ['哈登', '保罗', '维斯布鲁克']}
    return render(request, 'test_demo.html', context)

def test_demo2(request):
    context = {"ads": ["selenium", "appium", "requests"]
               }
    return render(request, 'test_demo2.html', context)

def login(request):
    '''登录页面'''
    if request.method == "GET":
        return render(request, 'login.html')
        # request.session['login_from'] = request.META.get('HTTP_REFERER', '/')

    if request.method == "POST":
        # 先查询数据库是否有此用户名
        username = request.POST.get('username')
        psw = request.POST.get('password')
        # 查询用户名和密码
        user_obj = User.objects.filter(user_name=username, psw=psw).first()
        if user_obj:
            return render(request, "index.html")
            # return redirect('/demo')
            # return HttpResponse('登陆成功')
            # return HttpResponseRedirect(request.session['login_from'])
        else:
            return HttpResponse('用户名或密码错误')