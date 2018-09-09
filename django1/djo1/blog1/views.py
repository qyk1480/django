from django.shortcuts import render,render_to_response

# Create your views here.


from django.http import HttpResponse

import datetime
'''
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
'''


def home(request):
    now = datetime.datetime.now()

    # html = "<html><body>It is now </body></html>"
    return render(request, 'index.html', locals())
    # return render(request, 'home.html', locals(),)
