from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
# 但是当第三方模块根本不知道你的user model在哪里如何导入呢
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class UserProfile(AbstractUser):
    name = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name='用户名')
    pwd = models.CharField(max_length=255, null=False, verbose_name='密码')
    phone = models.CharField(max_length=11, null=False, unique=True, verbose_name='电话号码')
    cardNum = models.CharField(max_length=18, null=False, unique=True, verbose_name='身份证号')
    birthday = models.DateTimeField(null=True, blank=True, verbose_name='出生年月')
    alias = models.CharField(max_length=50, null=True, blank=True, verbose_name='昵称')
    email = models.CharField(max_length=50, null=True, blank=True, verbose_name='邮箱')
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女'), ('secrecy', '保密')),
                              default='secrecy', verbose_name='性别')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name


class GoodsCategory(models.Model):
    # 商品分类
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),

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
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    sold_num = models.IntegerField(default=0, verbose_name="商品销售量")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")
    goods_num = models.IntegerField(default=0, verbose_name="库存数")
    market_price = models.FloatField(default=0, verbose_name="市场价格")

    member_price = models.FloatField(default=0, verbose_name="会员价格")
    goods_brief = models.TextField(max_length=500, verbose_name="商品简短描述")

    # 首页中新品展示
    is_new = models.BooleanField(default=False, verbose_name="是否新品")
    # 商品详情页的热卖商品，自行设置
    is_hot = models.BooleanField(default=False, verbose_name="是否热销")
    add_time = models.DateTimeField(auto_now=True, verbose_name="添加时间")
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, verbose_name="商品类目")

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class IndexAd(models.Model):
    """
    首页类别标签右边展示的七个商品广告
    """
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, related_name='category', verbose_name="商品类目")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='goods')

    class Meta:
        verbose_name = '首页广告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class HotSearchWords(models.Model):
    """
    搜索栏下方热搜词
    """
    keywords = models.CharField(default="", max_length=20, verbose_name="热搜词")
    index = models.IntegerField(default=0, verbose_name="排序")
    add_time = models.DateTimeField(auto_now=True, verbose_name="添加时间")

    class Meta:
        verbose_name = '热搜排行'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords


class OrderInfo(models.Model):
    """
    订单信息
    """
    ORDER_STATUS = (
        ('TRADE_SUCCESS', '成功'),
        ('TRADE_CLOSED', '超时关闭'),
        ('WAIT_BUYER_PAY', '交易创建'),
        ('TRADE_FINISHED', '交易结束'),
        ('paying', '待支付'),
    )

    PAY_TYPE = (
        ('alipay', '支付宝'),
        ('wechat', '微信'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    # unique 订单号唯一
    order_sn = models.CharField(max_length=30, unique=True, verbose_name='订单编号')
    # 微信支付
    nonce_str = models.CharField(max_length=50, unique=True, verbose_name='随机加密字符串')
    # 支付宝支付
    trado_no = models.CharField(max_length=100, unique=True, verbose_name='交易号')
    pay_status = models.CharField(choices=ORDER_STATUS, default='paying', max_length=30, verbose_name='支付状态')
    # 支付类型
    pay_type = models.CharField(choices=PAY_TYPE, default='alipay', max_length=10, verbose_name='支付类型')
    post_script = models.CharField(max_length=200, null=True, blank=True, verbose_name='订单备注')
    order_mount = models.FloatField(default=0.0, verbose_name='订单金额')
    pay_time = models.DateTimeField(auto_now_add=True, verbose_name='支付时间')

    # 用户信息
    address = models.CharField(max_length=100, default="", verbose_name="收货地址")
    signer_name = models.CharField(max_length=20, default="", verbose_name='签收人')
    signer_mobile = models.CharField(max_length=12, verbose_name='联系方式')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        ordering = ['pay_time']
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)


class OrderGoods(models.Model):
    """
    订单内商品信息
    """

    # 一个订单对应多个商品
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, verbose_name='订单信息', related_name='goods')
    # 两个外键形成一张关联表
    goods = models.ForeignKey(Goods,on_delete=models.DO_NOTHING, verbose_name="商品")
    goods_num = models.IntegerField(default=0, verbose_name="商品数量")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "订单内商品项"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)
