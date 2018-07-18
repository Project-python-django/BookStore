from django.db import models
import datetime


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




class GoodsCategory(models.Model):
    #商品分类
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
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, related_name='category',verbose_name="商品类目")
    goods =models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='goods')

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


class UserPrfile(models.Model):

    pass