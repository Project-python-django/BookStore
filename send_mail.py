#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 11:59
# @Author  : Alfred Pai
# @Email   : AlfredPai@outlook.com
# @File    : send_mail.py
# @Software: PyCharm

import os
from django.core.mail import send_mail, send_mass_mail

os.environ['DJANGO_SETTINGS_MODULE'] = "shop.settings"

if __name__ == '__main__':

    send_mail(
        '来自商城的测试邮件',  # 主题
        '<p>这是一封<strong>重要的</strong>邮件.</p><p>欢迎来我们的网上商城花钱买醉</p>',  # 内容
        'baifan1111@qq.com',  # 发送方
        ['1303676137@qq.com'],  # 接收方
        fail_silently=False,
    )