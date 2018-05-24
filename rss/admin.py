from django.contrib import admin

# Register your models here.
from .models import *
#model admin options
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["id","content",]
    #list_display_links = ["updated"]


    class Meta:
        model = News
admin.site.register(News, PostModelAdmin)

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["id","source", "date", "link", "title","content",]
    #list_display_links = ["updated"]


    class Meta:
        model = HimalayanTimes
admin.site.register(HimalayanTimes, PostModelAdmin)
