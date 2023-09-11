from django.contrib import admin
from django.urls import path
from seller import views

urlpatterns = [
   path("api/addSeller",views.addSeller,name='addSeller'),
   path("api/sellerLogin",views.sellerLogin,name='sellerLogin')
   # path("api/addShow",views.addShow,name='addShow'),
   
]