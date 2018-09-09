from django.shortcuts import render
from booktest.models import HeroInfo
from django.http import HttpResponse
from django.template import RequestContext


def index(request):
    # hero = HeroInfo.objects.get(pk=1)
    # context = {'hero': hero}
    list1 = HeroInfo.objects.filter(isDelete=False)
    context = {'list1': list1}
    return render(request, 'index.html', context)


def show(request, id1, id2):
    context = {'id1': id1, 'id2': id2}
    return render(request, 'show.html', context)


def index2(request):
    return render(request, 'index2.html')


def htmlTest(request):
    context = {'t1': '<h1>123</h1>'}
    return render(request, 'htmlTest.html', context)


def csrf1(request):
    return render(request, 'csrf.html')


def csrf2(request):
    uname = request.POST['uname']
    return HttpResponse(uname)
    # context = RequestContext(request, {'uname': uname})
    # return HttpResponse(context)


# 验证码
def verifycode(request):
    from PIL import Image, ImageDraw, ImageFont
    import random
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = '1234567890QWERTYUIOPASDFGHJKLZXCVBNM'
    rand_str = ''
    for i in range(4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象
    font = ImageFont.truetype('arial.ttf', 36)
    # font = ImageFont.truetype('FreeMono.ttf',23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    import io
    buf = io.StringIO()
    # 将文件保存在内存，类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')
