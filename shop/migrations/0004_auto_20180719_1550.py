# Generated by Django 2.0.7 on 2018-07-19 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20180719_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='orderAdress',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='ordergoods',
            name='goods',
        ),
        migrations.RemoveField(
            model_name='ordergoods',
            name='order',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderGoods',
        ),
    ]