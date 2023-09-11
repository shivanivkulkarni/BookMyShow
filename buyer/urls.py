from django.contrib import admin
from django.urls import path
from buyer import views

urlpatterns = [
   path("api/addCustomer",views.index,name='addCustomer'),
   path("api/addBuyer",views.addBuyer,name='addBuyer'),
   path("api/buyerLogin",views.buyerLogin,name='buyerLogin')

]