# Generated by Django 2.0.7 on 2018-07-19 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indexad',
            name='category',
        ),
        migrations.RemoveField(
            model_name='indexad',
            name='goods',
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='category_type',
            field=models.IntegerField(choices=[(1, '男装'), (2, '女装'), (3, '儿童'), (4, '运动')], help_text='类目级别', verbose_name='类目级别'),
        ),
        migrations.DeleteModel(
            name='IndexAd',
        ),
    ]
