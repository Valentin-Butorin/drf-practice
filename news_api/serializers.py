from rest_framework import serializers
from news_api.models import NewsItem, NewsType


class NewsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsType
        fields = ('id', 'name', 'color')


class NewsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem
        fields = ('id', 'title', 'description', 'content', 'type')
        depth = 1
