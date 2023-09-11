from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import login
from seller.models import *
import json
from App1.backends import *

# Create your views here.

@csrf_exempt
def addSeller(request):
    try:
        data = json.loads(request.body)
        fname = data.get('fname')
        lname = data.get('lname')
        email = data.get('email')
        password = data.get('password') 
        addSeller = Seller.objects.create_user(username = email, email = email,  password = password, first_name=fname, last_name = lname)
        # addticketSeller.save()
        # addTicketSeller.is_seller=True
        addSeller.save()
        return JsonResponse({"msg":"Ticket Seller added successfully"})
    except Exception as e:
        return JsonResponse({"msg":str(e)})

@csrf_exempt
def sellerLogin(request):
    try:
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        seller = SellerBackend().authenticate(request, username=email, password=password)
        print(seller)
        if seller is not None:
            seller.backend = 'django.contrib.auth.backends.ModelBackend'
            auth_login(request, seller)
            return JsonResponse({"msg": "Seller Login Successful"})
        else:
            return JsonResponse({"msg":"Please Enter Correct password or email"})

    except Exception as e:
        return JsonResponse({"msg":str(e)})





# @csrf_exempt
# def addShow(request):
#     try:
#         data = json.loads(request.body)
#         name = data.get('name')
#         location = data.get('location')
#         city=data.get('city')
#         date = data.get('date')
#         time = data.get('time')
#         ticketSeller_id = data.get('ticketSeller_id') 
#         addShow = Show(name = name, location = location,city=city, date = date, time = time, ticketSeller_id=ticketSeller_id)
#         addShow.save()
#         return JsonResponse({"msg":"Show added successfully"})
#     except Exception as e:
#         return JsonResponse({"msg":str(e)})



# # def about(request):
# #     return HttpResponse("this is about page")
