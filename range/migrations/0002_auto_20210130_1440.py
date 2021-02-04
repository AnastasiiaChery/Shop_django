# Generated by Django 3.1.5 on 2021-01-30 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('range', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsshoplist',
            name='description',
            field=models.CharField(max_length=1000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='goodsshoplist',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='goodsshoplist',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='goodsshoplist',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizzas', to='range.typegoods', verbose_name='Вид'),
        ),
        migrations.AlterField(
            model_name='goodsshoplist',
            name='weight',
            field=models.IntegerField(default=0, verbose_name='Вес'),
        ),
        migrations.AlterField(
            model_name='typegoods',
            name='types',
            field=models.CharField(max_length=10, verbose_name='Вид'),
        ),
    ]