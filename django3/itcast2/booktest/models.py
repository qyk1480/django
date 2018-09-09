from django.db import models

# Create your models here.


class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)

        def create(self, btitle, bpub_date):
            b = BookInfo()
            b.btitle = btitle
            b.bpub_date - bpub_date
            b.bread = 0
            b.bcommet = 0
            b.isDelete = False
            return b


class BookInfo(models.Model):
    # 指定管理器
    # books = models.Manager()

    btitle = models.CharField(max_length=20)
    # 重命名
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(null=False)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.btitle

    # 元信息
    class Meta:
        # 默认<app_name>_<model_name>, 重命名mysql表名
        db_table = 'bookinfo'
        # 加-表示倒序
        # ording = ['-id']

    books1 = models.Manager()
    books2 = BookInfoManager()

    # @classmethod
    # def create(cls, bittle, bpub_date):
    #   b=BookInfo()
    #   b.btitle = btitle
    #   b.bpub_date - bpub_date
    #   b.bread = 0
    #   b.bcommet = 0
    #   b.isDelete = False
    #   return b

    # book.heroinfo_set


class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)

    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.hname

    # hero.book.id
    # hero.book_id
