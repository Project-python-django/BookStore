<<<<<<< HEAD
import hashlib

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# 主页
from shop.models import ShAddress, Cart


def cart(req):
    user_id = req.session.get('is_login')
    # if not is_login:
    #     return render(req, 'login.html')

    # 查询当前用户的默认收货信息
    # deliveryAddress =ShAddress.objects.filter(user_id=is_login).first()

    # 查看当前用户下的购物车中的商品信息
    # carts = Cart.objects.filter(user_id=is_login)
    totalPrice = 0  # 计算总价格
    for cart in carts:
        if cart.isSelected:
            totalPrice += cart.goods.price * cart.cnt

    return render(req,
                  'cart.html',
                  {'myAddress': deliveryAddress,
                   'carts': carts,
                   'totalPrice': totalPrice})



def address(request):
    item=ShAddress.objects.all()
    return render(request,'address.html',{'item':item})
=======
import datetime
import hashlib

from django.shortcuts import render, redirect
from BookStore import settings
from . import models
from . import forms


# ----------业务----------


# 主页
def index(request):
    pass
    return render(request, 'shop/index.html')


# 密码加密
def hash_code(s, salt='shop'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


# 登录
def login(request):
    # 禁止重复登录
    if request.session.get('is_login', None):
        return redirect("/index/")
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容'
        if login_form.is_valid():
            # name = request.POST.get('name', None)
            # password = request.POST.get('password', None)
            name = login_form.cleaned_data['name']
            password = login_form.cleaned_data['password']
            # todo 用户名合法性验证
            # todo 密码长度验证
            try:
                user = models.User.objects.get(name=name)
                if not user.has_confonfirmed:
                    message = "请通过邮件确认登录"
                    return render(request, 'shop/login.html', locals())

                if len(password) < 8:
                    message = '密码长度过短，不安全'
                elif len(password) >= 8 and user.password == hash_code(password):
                    # 向session中写入用户状态和数据
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['name'] = user.name
                    return redirect('/index/')
                else:
                    message = "密码错误"
            except:
                message = "用户名不存在"
        # locals()函数，返回当前所有本地变量字典。
        return render(request, "shop/login.html", locals())

    login_form = forms.UserForm()
    return render(request, 'shop/login.html', locals())


# 生成验证码
def make_confirm_string(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.name, now)
    models.ConfirmString.objects.create(code=code, user=user, )
    return code


# 邮件
def send_email(email, code):
    from django.core.mail import EmailMultiAlternatives

    subject = '温州皮革厂倒闭了'

    text_content = '''感谢注册！'''

    html_content = '''
                    <p>感谢注册<a href="http://{}/confirm/?code={}" target=blank>www.taobao.com</a>，\
                    这里点击送小姨子！</p>
                    <p>请点击站点链接完成注册确认！</p>
                    <p>此链接有效期为{}天！</p>
                    '''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


# 注册
def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        message = '请检查输入内容'
        if register_form.is_valid():
            name = register_form.cleaned_data['name']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']

            if password1 != password2:
                message = "两次输入密码不同，请重新输入"
                return render(request, 'shop/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=name)
                if same_name_user:
                    message = "用户已经存在, 请重新选择用户名"
                    return render(request, 'shop/register.html', locals())

                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = "此邮箱已被注册"
                    return render(request, 'shop/register.html', locals())

                new_user = models.User()
                new_user.name = name
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                code = make_confirm_string(new_user)
                send_email(email, code)

                message = "请前往注册邮箱，进行邮箱注册"

                return render(request, 'shop/confirm.html', locals())

    register_form = forms.RegisterForm()
    return render(request, 'shop/register.html', locals())


# 验证验证码
def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm = models.ConfirmString.objects.get(code=code)
    except:
        message = '无效的确认请求!'
        return render(request, 'shop/confirm.html', locals())

    c_time = confirm.c_time
    now = datetime.datetime.now()
    if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = '您的邮件已经过期！请重新注册!'
        return render(request, 'shop/confirm.html', locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = '感谢确认，请使用账户登录！'
        return render(request, 'shop/confirm.html', locals())


# 登出
def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/index/')
    # flush()清空session
    request.session.flush()
    return redirect("/index/")
>>>>>>> bai
