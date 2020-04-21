from django.http import HttpResponse
from spider_page.models import longyitjzq

def slec_all(request):
    ret = longyitjzq.objects.all().values()
    return HttpResponse(ret)

