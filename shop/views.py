import datetime
import hashlib

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render, redirect
from BookStore import settings
from shop.models import ShAddress, Goods, Cart, User
from . import models
from . import forms


# ----------业务----------


# 主页
def index(request):
    pass
    return render(request, 'shop/home.html')


# 登录
def login(request):
    # 禁止重复登录
    if request.session.get('is_login', None):
        return redirect("/index/")
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容'
        if login_form.is_valid():
            name = login_form.cleaned_data['name']
            password = login_form.cleaned_data['password']
            # todo 用户名合法性验证
            # todo 密码长度验证
            try:
                user = models.User.objects.get(name=name)
            except:
                message = "用户不存在"
                return render(request, 'shop/login.html', locals())
            if not user.has_confonfirmed:
                message = "请通过邮件确认登录"
                return render(request, 'shop/login.html', locals())

            if user.password == hash_code(password):
                # 向session中写入用户状态和数据
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['name'] = user.name
                return redirect('/index/')
            else:
                message = "密码错误"
                return render(request, 'shop/login.html', locals())
        else:
            return render(request, 'shop/login.html', locals())
    # locals()函数，返回当前所有本地变量字典。
    login_form = forms.UserForm
    return render(request, "shop/login.html", locals())


# 密码加密
def hash_code(s, salt='shop'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


# 生成验证码
def make_confirm_string(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.name, now)
    models.ConfirmString.objects.create(code=code, user=user, )
    return code


# 邮件
def send_email(email, code):
    from django.core.mail import EmailMultiAlternatives

    subject = '魏明明~~~'

    text_content = '''非常感谢注册！'''

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

##############################################################

def cart(req):
    user_id = req.session.get('user_id')
    # if not user_id:
    #     return render(req, 'shop/login.html')

    # 查询当前用户的默认收货信息
    # deliveryAddress =ShAddress.objects.filter(user_id=user_id).first()
    #
    # #查看当前用户下的购物车中的商品信息
    # items = Cart.objects.filter(user_id=user_id)

    # totalPrice = 0  # 计算总价格
    # for item in items:
    #     if cart.isSelected:
    #         totalPrice += cart.goods.price * cart.cnt
    #
    # return render(req,
    #               'cart.html',
    #               {
    #                'items': items,
    #                'totalPrice': totalPrice})
    name=1
    price=10
    num=2
    sum=20
    totalPrice=30

    return render(req,'cart.html',{'name':1,'price':10,'num':2,'sum':20,'totalPrice':30})



def address(request):

    dz=ShAddress.objects.first()
    return render(request,'address.html',{'dz':dz})


def home(request):
    return render(request,'home.html')


def man(request):
    # man_list=Goods.objects.filter(cate='男装')
    man_list = Goods.objects.all()
    paginator = Paginator(man_list, 25)

    page = request.GET.get('page')
    try:
        mgoods = paginator.page(page)
    except PageNotAnInteger:
        # 如果请求的页数不是整数，返回第一页。
        mgoods = paginator.page(1)
    except EmptyPage:
        # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
        mgoods = paginator.page(paginator.num_pages)
    return render(request, 'man.html', {'mgoods': mgoods})

def woman(request):
    # woman_list=Goods.objects.filter(cate='女')
    woman_list = Goods.objects.all()
    paginator = Paginator(woman_list, 25)

    page = request.GET.get('page')
    try:
        wgoods = paginator.page(page)
    except PageNotAnInteger:
        # 如果请求的页数不是整数，返回第一页。
        wgoods = paginator.page(1)
    except EmptyPage:
        # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
        wgoods = paginator.page(paginator.num_pages)
    return render(request, 'man.html', {'wgoods': wgoods})


def selectCart(req, cart_id):
    # 0 全选， 99999 取消全选
    if cart_id == 0 or cart_id == 99999:
        # 全部更新
        carts = Cart.objects.filter(user_id=req.session.get('user_id'))
        carts.update(isSelected=True if cart_id == 0 else False)
        totalPrice = 0  # 统计全选时的总价格
        if cart_id == 0:
            for cart in carts:
                totalPrice += cart.cnt * cart.goods.price
        return JsonResponse({'price': totalPrice,
                             'status': 200})

    data = {'status': 200, 'price': 1000.5}
    try:
        cart = Cart.objects.get(id=cart_id)
        cart.isSelected = not cart.isSelected
        cart.save()
        data['price'] = cart.cnt * cart.goods.price
        data['selected'] = cart.isSelected  # 当前选择状态
    except:
        data['status'] = 300
        data['price'] = 0

    return JsonResponse(data)


def addCart(req, cart_id):
    # 添加指定cart_id的商品 cnt，如果cart_id不存在时，要新添加？
    price = 0
    qs = Cart.objects.filter(id=cart_id)
    if qs.exists():
        price = qs.first().goods.price
        qs.update(cnt=F('cnt') + 1)

    else:
        # 如果在Cart中查找不到，则表示cart_id为goods_id
        user_id = req.session.get('user_id');
        qs = Cart.objects.filter(user_id=user_id, goods_id=cart_id)
        if qs.exists():
            qs.update(cnt=F('cnt') + 1)
        else:
            qs.create(user_id=user_id, goods_id=cart_id, cnt=1)

        # 查看商品的单价
        price = Goods.objects.filter(productid=cart_id).first().price

    return JsonResponse({'status': 200,
                         'price': price,
                         'msg': '添加或更新购物车成功!'})


def subCart(req, cart_id):
    # 减去 指定cart_id的商品的cnt, 如果cnt为0时，要删除？
    price = 0
    data = {'status': 200, 'price': '10'}
    qs = Cart.objects.filter(id=cart_id)
    if qs.exists():
        price = qs.first().goods.price
        if qs.first().cnt > 0:
            qs.update(cnt=F('cnt') - 1)
            data['price'] = price
        else:
            data['price'] = '0'
            data['status'] = 201  # 不能再减了
    else:
        data['price'] = '0'
        data['status'] = 300  # 不存在

    return JsonResponse(data)

