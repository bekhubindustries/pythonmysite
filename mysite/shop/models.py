from django.db import models
from django.urls import reverse
from django import forms


# Create your models here.
class Shop(models.Model):
    name = models.CharField(verbose_name='Название товара', max_length=60)
    price = models.IntegerField(verbose_name='Цена товара ', )
    photo_path = models.ImageField(verbose_name='Картинка ', upload_to="photo/%Y/%M/%D/",
                                   default='2144250001_2_1_16.png')
    photo_path1 = models.ImageField(verbose_name='Картинка ', upload_to="photo/%Y/%M/%D/",
                                    default='2144250001_2_1_16.png')
    photo_path2 = models.ImageField(verbose_name='Картинка ', upload_to="photo/%Y/%M/%D/",
                                    default='2144250001_2_1_16.png')
    photo_path3 = models.ImageField(verbose_name='Картинка ', upload_to="photo/%Y/%M/%D/",
                                    default='2144250001_2_1_16.png')
    description = models.TextField(verbose_name='Описание', default='')
    description1 = models.TextField(verbose_name='Описание', default='')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товары',
        verbose_name = 'Товары',


class Category(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=60, db_index=True)

    def __str__(self):
        return self.name

    # class Meta:
    # verbose_name='Категория'
    # verbose_name='Категория'
