from django.db import models


"""
this class standars for table of database 
@TODO: register, display, updatade and delete.
and it holds for user authanication
e.g:name, email, phone, gender, role, username and password

"""
class Staff(models.Model):
    name = models.CharField(max_length= 255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    role = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)



"""
this class standars for table of database 
@TODO: register, display, updatade and delete.
and it holds for product details
e.g: product_name, product_cost, created_at

"""

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_cost = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)


"""
this class standars for table of database 
@TODO: register, display, updatade and delete.
and it holds for order throught customer 
e.g: procut id, user_id, quantity,total  price

"""

class Order(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    staff_id = models.ForeignKey(Staff, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()


"""
this class standars for table of database 
@TODO: register, display, updatade and delete.
and it holds for product details
e.g: payment_status, total_price, date, 

"""

class Transaction(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'


    PENDING_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE,'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]


    order_id = models.ForeignKey(Order, on_delete=Product)
    total_price = models.IntegerField()

    payment_status = models.CharField(max_length=1, choices=PENDING_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING )

    date = models.DateTimeField(auto_now=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.PROTECT)


    




