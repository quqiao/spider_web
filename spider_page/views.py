from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, reverse
import requests
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect

def index(request):
    return render(request, 'index.html', locals())  #

def page(request):
    return render(request, 'page.html')


def start(request):
    if request.method == 'POST':
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyPage', 'spider': 'longyi_tjzq'}
        print(requests.post(url=url, data=data))
        # res = request.post(url=url, data=data)
        # jobid = res['jobid']

        return JsonResponse({'result': 'ok'})