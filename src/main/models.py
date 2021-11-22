from django.db import models

from .utilities import get_timestamp_path


class Place(models.Model):
    """ Model of place """
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 verbose_name="Категория")
    title = models.CharField(max_length=32, verbose_name='Место')
    description = models.TextField(verbose_name="Описание")
    address = models.CharField(max_length=64, verbose_name='Адрес')
    image = models.ImageField(upload_to=get_timestamp_path,
                              verbose_name='Изображение')
    author = models.ForeignKey('users.AdvUser', on_delete=models.CASCADE,
                               verbose_name='Автор места'),
    city = models.ForeignKey(City, on_delete=models.PROTECT,
                             verbose_nmae="Город")
    is_active = models.BooleanField(default=True, db_index=True,
                                  verbose_name='Выводить в списке?')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True,
                                      verbose_name='Опубликовано')
    
    def delete(self, *args, **kwargs):
        """ Deleting additional images after removing place """
        for ai in self.additionalimage_set.all():
            ai.delete()
        super().delete(*args, **kwargs)


    class Meta:
        verbose_name_plural = 'Места'
        verbose_name = 'Место'
        ordering = ['-created_at']
