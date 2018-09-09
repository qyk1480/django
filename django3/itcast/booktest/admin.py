from django.contrib import admin

# Register your models here.
from booktest.models import Bookinfo, Heroinfo


class HeroinfoInline(admin.StackedInline):
    # 表格
    # class HeroinfoInline(admin.TabularInline):
    model = Heroinfo
    extra = 3


class BookinfoAdmin(admin.ModelAdmin):
    # 显示字段
    list_display = ['id', 'btitle', 'bpub_date']
    # 过滤字段
    list_filter = ['btitle']
    # 搜索字段
    search_fields = ['btitle']
    # 分页
    list_per_page = 2

    # 添加，修改页属性
    # 属性先后顺序，fields 和fieldsets不能同时使用
    # fields = ['bpub_date', 'btitle']

    # 属性分组
    fieldsets = [
                ('base', {'fields': ['btitle']}),
                ('super', {'fields': ['bpub_date']})
                ]

    inlines = [HeroinfoInline]


admin.site.register(Bookinfo, BookinfoAdmin)
admin.site.register(Heroinfo)
