from django.core.management.base import BaseCommand
from news_api.models import NewsType, NewsItem
from random import choice


class Command(BaseCommand):
    def handle(self, *args, **options):
        type_name_string = 'Наименование'
        color_string = 'Цвет'
        title_string = 'Заголовок'
        desc_string = 'Краткое описание'
        content_string = 'Контент'

        for i in range(1, 21):
            NewsType.objects.create(
                name=f'{type_name_string} {i}',
                color=f'{color_string} {i}',
            )

        types = NewsType.objects.all()

        for i in range(1, 201):
            NewsItem.objects.create(
                title=f'{title_string} {i}',
                description=f'{desc_string} {i}',
                content=f'{content_string} {i}',
                type=choice(types),
            )
