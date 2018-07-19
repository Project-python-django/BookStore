from django.db import models
import datetime






class GoodsCategory(models.Model):
    #商品分类
    CATEGORY_TYPE = (
        (1, "男装"),
        (2, "女装"),
        (3, "儿童"),
        (4, "运动"),

    )

    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")

    # 设置目录树的级别
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")

    add_time = models.DateTimeField(auto_now=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):

    goods_sn = models.CharField(max_length=50, default="", verbose_name="商品唯一货号")
    name = models.CharField(max_length=100, verbose_name="商品名")
    sold_num = models.IntegerField(default=0, verbose_name="商品销售量")
    goods_num = models.IntegerField(default=0, verbose_name="库存数")
    market_price = models.FloatField(default=0, verbose_name="市场价格")
    imgPath = models.CharField(max_length=100, default='',verbose_name="图片链接")

    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, verbose_name="商品类目")

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


#
# class HotSearchWords(models.Model):
#     """
#     搜索栏下方热搜词
#     """
#     keywords = models.CharField(default="", max_length=20, verbose_name="热搜词")
#     index = models.IntegerField(default=0, verbose_name="排序")
#     add_time = models.DateTimeField(auto_now=True, verbose_name="添加时间")
#
#     class Meta:
#         verbose_name = '热搜排行'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.keywords

class Cart(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)

    goods = models.ForeignKey(Goods,
                             on_delete=models.CASCADE)

    # 数量
    cnt = models.IntegerField(default=1)

    # 是否被选择
    isSelected = models.BooleanField(default=True)



class ShAddress(models.Model):
    # 收件地址模型类
    userName = models.CharField(max_length=20,
                            verbose_name='收件人')
    tel = models.CharField(max_length=12, verbose_name='收件人电话')
    streetName = models.TextField(default='',
                                      verbose_name='收货地址')

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)



# class Order(models.Model):  # 订单
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     # 订单的收货地址
#     orderAdress = models.ForeignKey(ShAddress,
#                                     on_delete=models.SET_NULL,
#                                     null=True)
#     # 订单的单号
#     orderNum = models.CharField(primary_key=True,
#                                 max_length=50, verbose_name='订单号')
#
#     # 生成订单时间
#     orderTime = models.DateTimeField(auto_now_add=True)
#
#
#
# class OrderGoods(models.Model):  # 订单明细
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     goods = models.ForeignKey(Goods, on_delete=models.SET_NULL, null=True)
#     cnt = models.IntegerField(default=1)
#     price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='小计')

