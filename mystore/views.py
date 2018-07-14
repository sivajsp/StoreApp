from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'product.html')
def prod_detail(request):
    return render(request,'product-detail.html')
def cart(request):
    return render(request,'cart.html')
