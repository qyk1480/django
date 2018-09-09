from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse


def index(request):

    response = HttpResponse('Hello')
    return response


def index2(request, arg):

    response = HttpResponse(arg)
    return response


def getTest1(request):
    return render(request, 'getTest1.html')


def getTest2(request):
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {'a':a1, 'b':b1, 'c':c1}
    return render(request, 'getTest2.html', context)


def getTest3(request):
    a1 = request.GET.getlist('a')
    b1 = request.GET['b']
    context = {'a':a1, 'b':b1}
    return render(request, 'getTest3.html', context)


def postTest1(request):
    return render(request, 'postTest1.html')


def postTest2(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST.get('ugender')
    uhobby = request.POST.getlist('uhobby')
    context = {'uname':uname, 'upwd':upwd, 'ugender':ugender, 'uhobby':uhobby}
    return render(request, 'postTest2.html', context)


def cookieTest(request):
    response = HttpResponse()
    cookie = request.COOKIES
    # response.set_cookie('t1','abc')
    if cookie.__contains__('t1'):
        response.write(cookie['t1'])

    return response


def redTest1(request):
    return HttpResponseRedirect('/redTest2/')
    # return redirect('/redTest2/')


def redTest2(request):
    return HttpResponse('重定向')


def jsonTest1(request):
    return JsonResponse({'list': 'abcd'})


# session
def session1(request):
    uname = request.session.get('myname', '未登录')
    # uname = request.session['myname']
    context = {'uname':uname}
    return render(request, 'session1.html', context)


def session2(request):
    return render(request, 'session2.html')


def session2_handle(request):
    uname = request.POST['uname']
    request.session['myname'] = uname
    request.session.set_expiry(0)
    return redirect('/session1/')


def session3(request):
    del request.session['myname']
    return redirect('/session1/')
