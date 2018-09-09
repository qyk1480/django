from django.contrib import admin
from booktest.models import *


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['btitle', 'bread', 'bpub_date', 'bcommet']


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['hname', 'hcontent', 'book']


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
