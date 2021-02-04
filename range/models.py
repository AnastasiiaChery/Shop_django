from django.db import models


# Create your models here.
class TypeGoods(models.Model):
    types = models.CharField(max_length=10, verbose_name='Вид')

    class Meta:
        db_table = 'goods_type'
        verbose_name = 'Список видов товаров'

    def __str__(self):
        return self.types


class GoodsShopList(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    price = models.IntegerField(default=0, verbose_name='Цена')
    description = models.CharField(max_length=1000, verbose_name='Описание')
    weight = models.IntegerField(default=0, verbose_name='Вес')
    type = models.ForeignKey(TypeGoods, on_delete=models.CASCADE, related_name='pizzas', verbose_name='Вид')
    photo = models.ImageField('Фото', upload_to='range/img', default='', blank=True)

    class Meta:
        db_table = 'goods_shop'
        verbose_name = 'Список товаров'

    def __str__(self):
        return self.name
