from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, reverse
import requests
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from spider_page.models import longyitjzq, rjyiyaoxpsj

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

def start_rjyiyao_xpsj(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'rjyiyao_xpsj'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result': 'ok'})  # {'result': 'ok'}

# def start_longyi_tjzq(request):
#     if request.method == 'POST':
#         # 启动爬虫
#         url = 'http://localhost:6800/schedule.json'
#         data = {'project': 'ScrapyPage', 'spider': 'longyi_tjzq'}
#         print(requests.post(url=url, data=data))
#         return JsonResponse({'result': 'ok'})  # {'result': 'ok'}
