from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField("标题", max_length=50)
    author = models.CharField("作者", max_length=50)
    created_date = models.DateField("创建时间", auto_now_add=True)
    modify_date = models.DateField("修改时间", auto_now=True)
    contents = models.TextField(max_length=100)
    public = models.BooleanField()

    class Meta:
        db_table = "article"

    def __str__(self):
        return self.title
