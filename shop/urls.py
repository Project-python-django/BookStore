
from django.urls import path, include

from shop import views

urlpatterns = [

    path('index/', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout"),
    # 图形验证码
    path('captcha', include('captcha.urls')),

    path('home/',views.home),
    path('cart/',views.cart),
    path('woman/',views.woman),
    path('man',views.man),
    path('lx',views.lx),
    path('gmxz',views.gmxz),
    path('order',views.order),
    # path('style',views.style),
]