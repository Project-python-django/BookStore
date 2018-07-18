from django.db import models


# Create your models here.
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

    user = models.ForeignKey(User,verbose_name="用户")
