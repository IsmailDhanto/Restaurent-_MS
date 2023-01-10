from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import *
from .forms import FormProduct



def index(request):
    context={}
    return render(request,"login.html",context)
def home(request):
    context={}
    return render(request,"index.html",context)
def product(request):
    form = FormProduct()
    all = Product.objects.all()    
    context = {
        "all":all,
        "form":form
    }
    return render(request,"products.html", context)


def order(request):
    products = Product.objects.all()
    context ={
        "products":products
    }
    return render(request, "order.html", context)

def new_order(request, id):
    return render(request, 'orderform.html')


def transaction(request):
    context = {}
    return render(request,"transaction.html", context)


def staff(request):
    context = {}
    return render(request, "staff.html", context)





def post_product(request):
    form = FormProduct()
    if request.method == 'POST':
        # pname = request.POST.get('product_name')
        # cost = request.POST.get('cost')
        # date = request.POST.get('date')
        # product = Product(product_name = pname, product_cost=cost,created_at=date)
        form = FormProduct(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            pname = product.product_name
            print(pname)
            product.save()
        # form = FormProduct(request.POST)
        
  
    return redirect('product')



def delete_product(request, id):
    product = Product.objects.get(id=id).delete()
    return redirect('product')

def update_product(request, pk):
    form = FormProduct()
    product = Product.objects.get(id=pk)
    form = FormProduct(instance=product)
    if request.method == 'POST':
        form = FormProduct(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product')
    context = {
        "form":form
    }

    return render(request, 'update.html', context)





