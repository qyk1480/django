from django.db import models

# Create your models here.


class Bookinfo(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Character(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(Bookinfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
