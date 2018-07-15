from django.shortcuts import render
from django.http import HttpResponse
from .models import storedb
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
def cart(request):
    return render(request,'cart.html')
