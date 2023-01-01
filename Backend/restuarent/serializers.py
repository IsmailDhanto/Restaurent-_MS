from rest_framework import serializers
from .models import *

"""
this class is serializers for product table
"""
class Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','product_name', 'product_cost', 'created_at' ]




"""
this class is serializers for Staff table
"""

class Staff_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'name', 'email','phone', 'gender', 'role', 'username', 'password']


"""
this class is serializers for Order table
"""

class Order_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'product_id', 'staff_id', 'quantity']


"""
this class is serializers for Transaction table
"""

class Transaction_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'order_id', 'total_price', 'payment_status', 'date', 'staff_id']

