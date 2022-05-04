from rest_framework.routers import DefaultRouter
from news_api.api import NewsItemViewset, NewsTypeViewset

app_name = 'news_api'

router = DefaultRouter()
router.register('articles', NewsItemViewset, basename='articles')
router.register('types', NewsTypeViewset, basename='types')
urlpatterns = router.urls


