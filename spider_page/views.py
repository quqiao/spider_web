from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, reverse
import requests
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from spider_page.models import longyitjzq, rjyiyaoxpsj, rjyiyaozkzq, \
                               scjrmzszq, scjuchuangyxzq, sckxyyypzq, scytyyzszq, \
                                ysbangzxxd,hezongyypy,scjuchuangtjzq,scjuchuangpy, longyiyp,scytyytjzq

def index(request):
    return render(request, 'index.html', locals())  # , locals()

def page(request):
    return render(request, 'page.html')

"""合纵药易购——普药专区"""
def hezongyy_py(request):
    users = hezongyypy.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'hezongyy_py.html', {'users': users})
def start_hezongyy_py(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'hezongyy_py'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})

"""龙一医药网——特价专区"""
def longyi_tjzq(request):
    users = longyitjzq.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'longyi_tjzq.html', {'users': users})
def start_longyi_tjzq(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'longyi_tjzq'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})
"""龙一医药网——药品专区"""
def longyi_yp(request):
    users = longyiyp.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'longyi_yp.html', {'users': users})
def start_longyi_yp(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'longyi_yp'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})

"""蓉锦医药网——新品上架"""
def rjyiyao_xpsj(request):
    users = rjyiyaoxpsj.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'rjyiyao_xpsj.html', {'users': users})
def start_rjyiyao_xpsj(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'rjyiyao_xpsj'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})

"""蓉锦医药网——折扣专区"""
def rjyiyao_zkzq(request):
    users = rjyiyaozkzq.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'rjyiyao_zkzq.html', {'users': users})
def start_rjyiyao_zkzq(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'rjyiyao_zkzq'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})

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
