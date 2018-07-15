from django.shortcuts import render
from django.http import HttpResponse
from .models import storedb,cartdb
from .forms import addingtocart
from django.core.exceptions import ObjectDoesNotExist
def index(request):
    x = storedb.objects.all()
    context = {'prod':x}
    return render(request,'product.html',context)
def category(request,categ):
    x = storedb.objects.filter(Category=categ)
    context = {'prod':x}
    return render(request,'product.html',context)
def prod_detail(request,name):
    if(request.method == "POST"):
         y = addingtocart(request.POST)
         if(y.is_valid()):
             try:
                 z = cartdb.objects.get(product=name)
                 z.count = z.count + y.count
                 z.save()
             except ObjectDoesNotExist:
                 z = cartdb(product=name,count=y.count)

    x = storedb.objects.get(product=name)
    cform = addingtocart()
    context = {'productd':x,'form':cform}
    return render(request,'product-detail.html',context)
def cart(request):
    return render(request,'cart.html')
