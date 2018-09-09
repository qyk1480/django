from django.contrib import admin
from booktest.models import HeroInfo, BookInfo


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']


@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['hname', 'hgender', 'hcontent']


admin.site.register(BookInfo, BookInfoAdmin)
# admin.site.register(HeroInfo, HeroInfoAdmin)
