from django.shortcuts import render

from django.db.models import Max, F, Q
from booktest.models import BookInfo


def index(request):
    list1 = BookInfo.books1.filter(pk__lt=3)
    max1 = BookInfo.books1.aggregate(Max('bpub_date'))
    list2 = BookInfo.books1.filter(bread__lt=F('bcommet') / 2)
    list3 = BookInfo.books1.filter(Q(bread=58) | Q(bread=12))
    context = {
        'list1': list1,
        'max1': max1,
        'list2': list2,
        'list3': list3
                }
    return render(request, 'index.html', context)
