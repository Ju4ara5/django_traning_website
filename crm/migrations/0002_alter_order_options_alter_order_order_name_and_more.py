# Generated by Django 4.0.1 on 2022-03-20 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterField(
            model_name='order',
            name='order_name',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_phone',
            field=models.CharField(max_length=200, verbose_name='Телефон'),
        ),
    ]