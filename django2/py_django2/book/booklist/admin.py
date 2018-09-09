from django.contrib import admin

from booklist.models import Bookinfo, Character
# Register your models here.


class CharacterAdmin(admin.ModelAdmin):
    # 列表页显示的字段
    list_display = ['id', 'name', 'gender', 'book']


admin.site.register(Bookinfo)

admin.site.register(Character, CharacterAdmin)
