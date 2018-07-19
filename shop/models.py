from django.db import models

# 用户类
class User(models.Model):

<<<<<<< HEAD
class UserProfile(models.Model):
    SEXCHOICE = (('male', '男'),('female', '女'))
    name = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=255, null=False, verbose_name='密码')
    phone = models.CharField(max_length=11, null=False, unique=True, verbose_name='电话号码')
    cardNum = models.CharField(max_length=18, null=False, unique=True, verbose_name='身份证号')
    birthday = models.DateTimeField(null=True, blank=True, verbose_name='出生年月')
    alias = models.CharField(max_length=50, null=True, blank=True, verbose_name='昵称')
    email = models.CharField(max_length=50, null=True, blank=True, verbose_name='邮箱')
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女'), ('secrecy', '保密')),
                              default='secrecy', verbose_name='性别')
=======
    gender = (('male', '男'), ('female', '女'))
    name = models.CharField(max_length=256, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="male")
    c_time = models.DateTimeField(auto_now_add=True)
    has_confonfirmed = models.BooleanField(default=False)
>>>>>>> bai

    # 使用__str__帮助人性化显示对象信息；
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = verbose_name

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