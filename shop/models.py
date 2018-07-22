from django.db import models


# 用户类
class User(models.Model):
    gender = (('male', '男'), ('female', '女'))
    name = models.CharField(max_length=254, unique=True)
    password = models.CharField(max_length=254)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="male")
    c_time = models.DateTimeField(auto_now_add=True)
    has_confonfirmed = models.BooleanField(default=False)

    # 使用__str__帮助人性化显示对象信息；
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = verbose_name


class ConfirmString(models.Model):
    code = models.CharField(max_length=254, verbose_name="确认码")
    user = models.OneToOneField("User", on_delete=models.DO_NOTHING, verbose_name='关联的用户')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='创建的时间')

    def __str__(self):
        return self.user.name + ":  " + self.code

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "验证码"
        verbose_name_plural = verbose_name


class Goods(models.Model):
    g_id = models.CharField(max_length=50, default="", verbose_name="商品唯一货号")
    cate = models.CharField(max_length=100, verbose_name='类型')
    image = models.CharField(max_length=200, verbose_name="图片路径")
    price = models.CharField(max_length=10, verbose_name="市场价格")
    number = models.CharField(max_length=100, verbose_name="库存数量")
    title = models.CharField(max_length=100, verbose_name="商品名程")
    location = models.CharField(max_length=100, verbose_name="商品产地")

    class Meta:
        db_table = 'taobao'
        verbose_name = "用户"
        verbose_name_plural = verbose_name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    # 数量
    cnt = models.IntegerField(default=1)
    # 是否被选择
    isSelected = models.BooleanField(default=True)



class ShAddress(models.Model):
    # 收件地址模型类
    userName = models.CharField(max_length=20, verbose_name='收件人')
    tel = models.CharField(max_length=12, verbose_name='收件人电话')
    streetName = models.TextField(default='', verbose_name='收货地址')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# 顾客投诉与建议
class Contact(models.Model):
    usernsme = models.CharField(max_length=20, verbose_name='姓名')
    email = models.CharField(max_length=30, verbose_name='邮箱')
    title = models.CharField(max_length=30, verbose_name='主题')
    content = models.CharField(max_length=250, verbose_name='内容')

    class Meta:
        verbose_name = "投诉建议"
        verbose_name_plural = verbose_name
