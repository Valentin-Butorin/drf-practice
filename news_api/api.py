from rest_framework import viewsets
from news_api.serializers import NewsItemSerializer, NewsTypeSerializer
from news_api.models import NewsItem, NewsType


class NewsItemViewset(viewsets.ModelViewSet):
    serializer_class = NewsItemSerializer

    def get_queryset(self):
        queryset = None
        type_id = self.request.query_params.get('type_id')
        if type_id is not None:
            if type_id.isdigit():
                queryset = NewsItem.objects.filter(type_id=type_id).select_related('type')
        else:
            queryset = NewsItem.objects.select_related('type')

        return queryset


class NewsTypeViewset(viewsets.ModelViewSet):
    serializer_class = NewsTypeSerializer

    def get_queryset(self):
        return NewsType.objects
