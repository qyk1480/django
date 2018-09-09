from django.shortcuts import render
from django.http import JsonResponse
from booktest.models import AreaInfo, Tinymce1


def index(request):
    return render(request, 'index.html')


def pro(request):
    prolist = AreaInfo.objects.filter(parea__isnull=True)
    list1 = []
    # [[1,'北京'],[2,'天津']...]
    for item in prolist:
        list1.append([item.id, item.title])

    return JsonResponse({'data': list1})


def city(request, id):
    citylist = AreaInfo.objects.filter(parea_id=id)
    list1 = []
    # [{id:1,title:北京}，..]
    for item in citylist:
        list1.append({'id': item.id, 'title': item.title})
    return JsonResponse({'data': list1})


# 自定义编辑器
def htmlEditor(request):
    return render(request, 'htmlEditor.html')


def htmlEditorHandle(request):
    html = request.POST['hcontent']
    # 添加
    tinymce1 = Tinymce1()
    tinymce1.content = html
    # tinymce1.save

    # 修改
    # tinymce1 = Tinymce1.objects.get(pk=1)
    # tinymce1.content = html

    # 存入数据库
    tinymce1.save()
    context = {'context': html}
    return render(request, 'htmlShow.html', context)


# 全文检索+中文分词
def mysearch(request):
    return render(request, 'mysearch.html')
