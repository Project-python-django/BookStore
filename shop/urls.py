
from django.urls import path

from shop import views

urlpatterns = {

    path('address/',views.address),
    path('cart/',views.cart)


}
