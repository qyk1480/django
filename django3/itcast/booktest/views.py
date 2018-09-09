from django.shortcuts import render

from django.http import HttpResponse
# from django.template import RequestContext, loader
from booktest.models import Bookinfo, Heroinfo

# Create your views here.


def index(request):
    # temp = loader.get_template('index.html')
    # return HttpResponse(temp.render())

    bookList = Bookinfo.objects.all()
    context = {'title': 'weather', 'list': bookList}
    response = render(request, 'index.html', context)

    return response


def show(request, hero_id):
    book = Bookinfo.objects.get(pk=hero_id)
    heroList = book.heroinfo_set.all()
    context = {'list': heroList}
    response = render(request, 'show.html', context)
    return response
