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