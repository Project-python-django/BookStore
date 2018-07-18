from django.urls import path

from shop import views

urlpatterns = [
    # 订单
    path('order/', views.login, name='order'),
    # http://localhost:8000/login/
    path('login/', views.login, name="login"),
    # http://localhost:8000/logout/
    path('logout/', views.logout, name="logout"),
    path('home/',views.home),
]