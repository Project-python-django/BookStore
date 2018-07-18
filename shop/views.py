from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext

from .models import UserProfile


class UserForm(forms.Form):
    name = forms.CharField(label='用户名', max_length=30)
    password = forms.CharField(label='密码1', widget=forms.PasswordInput())
    password2 = forms.CharField(label='密码2', widget=forms.PasswordInput())
    phone = forms.CharField(label='电话', max_length=11)
    cardNum = forms.CharField(label='身份证')
    birthday= forms.DateTimeField(label='生日', input_formats="%Y-%m-%d")
    alias = forms.CharField(max_length=50)
    email = forms.EmailField(label='邮箱', max_length=50)
    gender = forms.ChoiceField(label='性别2', choices=(('male','男'), ('female', '女'), ('secrecy', '保密')))


    def __str__(self):
        return self.name

# 主页
def home(request):
    return HttpResponse("这是主页")


# -------------------用户业务-------------------
#  注册功能
def regist(request):
    Method = request.method
    if Method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data['name']
            if userform.password == userform.password2:
                password = userform.cleaned_data['password']
            phone = userform.cleaned_data['phone']
            cardNum = userform.cleaned_data['cardNum']


            try:
                registJudge = UserProfile.objects.filter(name=name).get().name
                return render(request, 'regist.html', {'registJudge': registJudge})
            except:
                registAdd = UserProfile.objects.create(name=name, password=password)
                return render(request, 'regist.html', {'registAdd': registAdd, 'name': name})
    else:
        userform = UserForm()
    return render(request, 'regist.html', {'userform': userform, 'Method':Method})



# todo 登录
def login(request):
    return HttpResponse("这是登录页面")


# todo 登出
def logout(request):
    return HttpResponse("这是退出页面")
