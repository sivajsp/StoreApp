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
    x = storedb.objects.get(product=name)
    context = {'productd':x}
    return render(request,'product-detail.html',context)
def prod_detail1(request,name,count1):
    try:
        z = cartdb.objects.get(product=name)
        z.count += count1
        z.save()
    except ObjectDoesNotExist:
        y = cartdb(product=name,count = count1)
        y.save()
    print("hi")
    x = storedb.objects.get(product=name)
    context = {'productd':x}
    return render(request,'product-detail.html',context)
def cart(request):
    x = cartdb.objects.all()
    context = {'cart':x}
    return render(request,'cart.html',context)
