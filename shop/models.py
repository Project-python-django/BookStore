from datetime import datetime

from django.db import models


# Create your models here.
class UserProfile:
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

    user = models.ForeignKey(UserProfile, verbose_name="用户")
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
    order = models.ForeignKey(OrderInfo, verbose_name='订单信息', related_name='goods')
