from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name = "index"),
    path("product-detail",views.prod_detail,name = "product-detail"),
    path("cart",views.cart , name  = "cart"),
]
