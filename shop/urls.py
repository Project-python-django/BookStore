
from django.urls import path, include

from shop import views

urlpatterns = [

    path('index/', views.index, name="index"),
    path('home/login/', views.login, name="login"),
    path('home/register/', views.register, name="register"),
    path('home/logout/', views.logout, name="logout"),
    # 图形验证码
    path('captcha', include('captcha.urls')),
    path('home/',views.home),
    path('home/cart/',views.cart),
    path('home/address',views.address),

    path('man',views.man),

    path('woman',views.woman)
    #############

]