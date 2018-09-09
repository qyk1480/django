from django.db import models


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    # 重命名
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(null=False)
    isDelete = models.BooleanField(default=False)

    # 元信息
    class Meta:
        # 默认<app_name>_<model_name>, 重命名mysql表名
        db_table = 'bookinfo'
        # 加-表示倒序
        # ording = ['-id']


class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)

    book = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

    def showname(self):
        return self.hname
