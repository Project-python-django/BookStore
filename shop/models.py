from django.db import models

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