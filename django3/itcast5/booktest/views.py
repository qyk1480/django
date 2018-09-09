from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from booktest.models import HeroInfo, AreaInfo
from django.core.paginator import Paginator
import os


def index(request):
    return render(request, 'index.html')


def myexp(request):
    # a1 = int('asd')
    return HttpResponse('Hello')


def uploadPic(request):
    return render(request, 'uploadPic.html')


def uploadHandle(request):
    pic1 = request.FILES['pic1']
    picName = os.path.join(settings.MEDIA_ROOT, pic1.name)
    with open(picName, 'wb') as pic:
        for c in pic1.chunks():
            pic.write(c)
    return HttpResponse('<img src="\\static\\media\\%s" />' % pic1.name)


def herolist(request, pindex):
    if pindex == '':
        pindex = '1'

    list1 = HeroInfo.objects.all()
    pagin = Paginator(list1, 5)
    page = pagin.page(int(pindex))
    context = {'page': page}
    return render(request, 'herolist.html', context)


# 省市区选择
def area(request):
    return render(request, 'area.html')


def area2(request, id):
    id1 = int(id)
    if id1 == 0:
        data = AreaInfo.objects.filter(parea__isnull=True)
    else:
        data = [{}]

    list2 = []
    for area in data:
        list2.append([area.id, area.title])

    data1 = {'data': list2}
    return JsonResponse(data1)
