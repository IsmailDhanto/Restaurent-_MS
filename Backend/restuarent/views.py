from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import *
from .serializers import *



def index(request):
    context={}
    return render(request,"login.html",context)
def home(request):
    context={}
    return render(request,"index.html",context)
def product(request):
    
    all = Product.objects.all()    
    get_serializer = Product_Serializer(all, many = True)
    context = {
        "all":all
    }
    return render(request,"products.html", context)


def order(request):
    context ={}
    return render(request, "order.html", context)




def transaction(request):
    context = {}
    return render(request,"transaction.html", context)


def staff(request):
    context = {}
    return render(request, "staff.html", context)


@api_view(['GET'])
def get_products(request):

    get_product = Product.objects.all()
    get_serializer = Product_Serializer(get_product, many = True)

    return JsonResponse({
        "succsess": True,
        "products":get_serializer.data

    })



def post_product(request):
    post_prd = request.POST['']
# Create your views here.
