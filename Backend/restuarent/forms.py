from django.forms import ModelForm
from .models import *





class FormProduct(ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'