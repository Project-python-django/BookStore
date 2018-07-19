from django.db import models
import datetime

# 用户类
class User(models.Model):

    gender = (('male', '男'), ('female', '女'))
    name = models.CharField(max_length=256, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="male")
    c_time = models.DateTimeField(auto_now_add=True)
    has_confonfirmed = models.BooleanField(default=False)


    # 使用__str__帮助人性化显示对象信息；
    def __str__(self):
        return self.name

class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name+":  "+self.code

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "验证码"
        verbose_name_plural = verbose_name


class Goods(models.Model):

    goods_id = models.CharField(max_length=50, default="", verbose_name="商品唯一货号")
    name = models.CharField(max_length=100, verbose_name="商品名")
    sold_num = models.IntegerField(default=0, verbose_name="商品销售量")
    goods_num = models.IntegerField(default=0, verbose_name="库存数")
    market_price = models.FloatField(default=0, verbose_name="市场价格")
    imgPath = models.CharField(max_length=100, default='',verbose_name="图片链接")


    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name



class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    goods = models.ForeignKey(Goods,on_delete=models.CASCADE)

    # 数量
    cnt = models.IntegerField(default=1)

    # 是否被选择
    isSelected = models.BooleanField(default=True)



class ShAddress(models.Model):
    # 收件地址模型类
    userName = models.CharField(max_length=20,verbose_name='收件人')
    tel = models.CharField(max_length=12, verbose_name='收件人电话')
    streetName = models.TextField(default='',verbose_name='收货地址')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

