from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import *
from .serializers import *


def index(request):
    context={}
    return render(request,"index.html",context)
def home(request):
    context={}
    return render(request,"indexq.html",context)

@api_view(['GET'])
def get_products(request):

    get_product = Product.objects.all()
    get_serializer = Product_Serializer(get_product, many = True)

    return JsonResponse({
        "succsess": True,
        "products":get_serializer.data

    })


# Create your views here.
