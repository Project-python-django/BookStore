from django.urls import path, include

from shop import views

urlpatterns = [
<<<<<<< HEAD
    # http://localhost:8000/shop/regist/
    path('regist/', views.regist, name="register"),
    # http://localhost:8000/shop/login/
    path('login/', views.login, name="login"),
    # http://localhost:8000/shop/logout/
    path('logout/', views.logout, name="logout"),

=======
    path('index/', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('register', views.register, name="register"),
    path('logout/', views.logout, name="logout"),
    # 图形验证码
    path('captcha', include('captcha.urls')),
>>>>>>> bai
]
