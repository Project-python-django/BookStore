# Generated by Django 2.0.7 on 2018-07-19 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20180719_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnt', models.IntegerField(default=1)),
                ('isSelected', models.BooleanField(default=True)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderNum', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='订单号')),
                ('orderTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnt', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='小计')),
                ('goods', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Goods')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Order')),
            ],
        ),
        migrations.CreateModel(
            name='ShAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=20, verbose_name='收件人')),
                ('tel', models.CharField(max_length=12, verbose_name='收件人电话')),
                ('streetName', models.TextField(default='', verbose_name='收货地址')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=32)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['-c_time'],
            },
        ),
        migrations.DeleteModel(
            name='HotSearchWords',
        ),
        migrations.DeleteModel(
            name='UserPrfile',
        ),
        migrations.AddField(
            model_name='shaddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.User'),
        ),
        migrations.AddField(
            model_name='order',
            name='orderAdress',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.ShAddress'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.User'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.User'),
        ),
    ]
