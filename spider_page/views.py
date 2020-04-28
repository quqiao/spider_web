from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, reverse
import requests
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from spider_page.models import longyitjzq, rjyiyaoxpsj, rjyiyaozkzq, scjrmzszq, scjuchuangyxzq, sckxyyypzq, scytyyzszq, ysbangzxxd

def index(request):
    return render(request, 'index.html', locals())  # , locals()

def page(request):
    return render(request, 'page.html')

def longyi_tjzq(request):
    users = longyitjzq.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'longyi_tjzq.html', {'users': users})
    # return render(request, 'longyi_tjzq.html')

def rjyiyao_xpsj(request):
    users = rjyiyaoxpsj.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'rjyiyao_xpsj.html', {'users': users})

def rjyiyao_zkzq(request):
    users = rjyiyaozkzq.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'rjyiyao_zkzq.html', {'users': users})

def scjrm_zszq(request):
    users = scjrmzszq.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'scjrm_zszq.html', {'users': users})

def scjuchuang_yxzq(request):
    users = scjuchuangyxzq.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'scjuchuang_yxzq.html', {'users': users})

def sckxyy_ypzq(request):
    users = sckxyyypzq.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'sckxyy_ypzq.html', {'users': users})

def scytyy_zszq(request):
    users = scytyyzszq.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'scytyy_zszq.html', {'users': users})

def ysbang_zxxd(request):
    users = ysbangzxxd.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'ysbang_zxxd.html', {'users': users})

def start_longyi_tjzq(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'longyi_tjzq'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})

def start_rjyiyao_xpsj(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'rjyiyao_xpsj'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})

def start_rjyiyao_zkzq(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'rjyiyao_zkzq'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})

def start_scjrm_zszq(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'scjrm_zszq'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})

def start_scjuchuang_yxzq(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'scjuchuang_yxzq'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})

def start_sckxyy_ypzq(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'sckxyy_ypzq'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})

def start_scytyy_zszq(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'scytyy_zszq'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})

def start_ysbang_zxxd(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'ysbang_zxxd'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})
