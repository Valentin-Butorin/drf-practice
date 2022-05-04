from django.db import models


class NewsType(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name='Наименование',
    )
    color = models.CharField(
        max_length=64,
        verbose_name='Цвет',
    )

    class Meta:
        verbose_name = 'Тип новости'
        verbose_name_plural = 'Типы новостей'

    def __str__(self):
        return self.name


class NewsItem(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок',
    )
    description = models.CharField(
        max_length=255,
        verbose_name='Краткое описание',
    )
    content = models.TextField(
        verbose_name='Текст',
    )
    type = models.ForeignKey(
        NewsType,
        on_delete=models.PROTECT,
        related_name='news',
        verbose_name='Тип новости'
    )

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
