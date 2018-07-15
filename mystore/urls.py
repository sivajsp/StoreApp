from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name = "index"),
    path("product-detail/<str:name>",views.prod_detail,name = "product-detail"),
    path("product-detail/<str:name>/<int:count1>",views.prod_detail1,name = "product-detail1"),
    path("cart",views.cart , name  = "cart"),
    path("<str:categ>",views.category,name="index-cate")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
