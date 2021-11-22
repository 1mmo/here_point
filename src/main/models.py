from django.db import models

from .utilities import get_timestamp_path


class Place(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 verbose_name="Категория")
    title = models.CharField(max_length=32, verbose_name='Место')
    description = models.TextField(verbose_name="Описание")    
