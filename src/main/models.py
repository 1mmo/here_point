from django.db import models

from .utilities import get_timestamp_path
from users.models import AdvUser


class Comment(models.Model):
    """ Model of comment """
    place = models.ForeignKey("Place", on_delete=models.CASCADE, 
                              verbose_name='Место')
    author = models.CharField(max_length=30, default='Гость', verbose_name='Автор')
    content = models.TextField(verbose_name='Содержание')
    is_active = models.BooleanField(default=True, db_index=True,
                                    verbose_name='Выводить на экран?')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True,
                                      verbose_name='Опубликовано')

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'
        ordering = ['created_at']


class Place(models.Model):
    """ Model of place """
    categories = models.ManyToManyField("Category", verbose_name='Категория')
    title = models.CharField(max_length=32, verbose_name='Место')
    description = models.TextField(verbose_name="Описание")
    address = models.CharField(max_length=64, verbose_name='Адрес')
    image = models.ImageField(upload_to=get_timestamp_path,
                              verbose_name='Изображение')
    author = models.ForeignKey(AdvUser, on_delete=models.CASCADE,
                               null=True, blank=False, 
                               verbose_name='Автор места')
    city = models.ForeignKey("City", on_delete=models.PROTECT,
                             verbose_name="Город")
    is_active = models.BooleanField(default=True, db_index=True,
                                  verbose_name='Выводить в списке?')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True,
                                      verbose_name='Опубликовано')

    def _categories(self):
        return ", ".join([category.title for category in self.categories.all()])

    def delete(self, *args, **kwargs):
        """ Deleting additional images after removing place """
        for ai in self.additionalimage_set.all():
            ai.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name_plural = 'Места'
        verbose_name = 'Место'
        ordering = ['-created_at']


class AdditionalImage(models.Model):
    """ Additional image model """
    place = models.ForeignKey("Place", on_delete=models.CASCADE,
                              verbose_name='Место')
    image = models.ImageField(upload_to=get_timestamp_path,
                              verbose_name='Изображение')

    
    class Meta:
        verbose_name_plural = 'Дополнительные иллюстрации'
        verbose_name = 'Дополнительная иллюстрация'


class City(models.Model):
    title = models.CharField(max_length=32, verbose_name='Город')
    order = models.SmallIntegerField(default=0, db_index=True,
                                     verbose_name='Порядок')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = 'Города'
        verbose_name = 'Город'


class Category(models.Model):
    """ Category model """
    title = models.CharField(max_length=32, db_index=True, unique=True,
                             verbose_name='Название')
    order = models.SmallIntegerField(default=0, db_index=True,
                                     verbose_name='Порядок')

    def __str__(self):
        return self.title


    class Meta:
        ordering = ('order', 'title')
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class AdvUser(AdvUser):
    def delete(self, *args, **kwargs):
        for p in self.place_set.all():
            p.delete()
        super().delete(*args, **kwargs)
