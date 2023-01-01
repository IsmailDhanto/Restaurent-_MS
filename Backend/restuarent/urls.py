from django.urls import path
from restuarent import views

urlpatterns = [
    
    path("",views.index,name="Index"),
    path("home/",views.home,name="home")
]
