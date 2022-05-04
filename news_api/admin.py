from django.contrib import admin
from news_api.models import NewsType, NewsItem


@admin.register(NewsType)
class NewsTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color')


@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'title', 'description')
