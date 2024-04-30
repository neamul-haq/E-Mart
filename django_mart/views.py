from django.shortcuts import render
from store.models import Product
def home(request):
    product= Product.objects.all()
    return render (request,'index.html',{'product':product})
   