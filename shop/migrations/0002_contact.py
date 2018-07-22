# Generated by Django 2.0.7 on 2018-07-22 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usernsme', models.CharField(max_length=20, verbose_name='姓名')),
                ('email', models.CharField(max_length=30, verbose_name='邮箱')),
                ('title', models.CharField(max_length=30, verbose_name='主题')),
                ('content', models.CharField(max_length=250, verbose_name='内容')),
            ],
            options={
                'verbose_name': '投诉建议',
                'verbose_name_plural': '投诉建议',
            },
        ),
    ]