from django.shortcuts import render

from django.http import HttpResponse
from booklist.models import Bookinfo, Character
# Create your views here.


def bookList(request):
    # html {{key}} 代替
    blist = Bookinfo.objects.all()
    context = {
        'blist': blist
    }

    response = render(request, 'book.html', context)
    return response


def characterList(request, book_id):
    clist = Bookinfo.objects.get(id=book_id)
    c_list = clist.character_set.all()

    context = {
     'c_list': c_list
        }

    response = render(request, 'hito.html', context)
    return response
