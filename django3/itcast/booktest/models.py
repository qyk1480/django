from django.db import models


# Create your models here.
class Bookinfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()

    # objects显示
    def __str__(self):
        return self.btitle
        # self.btitle.encode('utf-8')


class Heroinfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    # ForeignKey需要on_delete
    hbook = models.ForeignKey(Bookinfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.hname


# python manage.py shell

# from booktest.models import *
# b = Bookinfo()
# b.btitle = 'asd'

# from datetime import datetime
# b.bpub_date = datetime(year=1990, month=1, day=12)
# b.save()

# Bookinfo.objects.all()
