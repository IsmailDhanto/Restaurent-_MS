from django.urls import path
from restuarent import views

urlpatterns = [
    
    path("",views.index,name="Index"),
    path("home/",views.home,name="home"),
    path("product/",views.product, name="product"),
    path("order/",views.order, name="order"),
    path("transaction/",views.transaction, name="transaction"),
    path("staff/",views.staff, name="staff"),
    path("post_product/",views.post_product, name='post_product')
]
