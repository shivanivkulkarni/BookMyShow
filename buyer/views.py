from django.shortcuts import render
from buyer.models import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login
from buyer.models import *
import json
from django.http import JsonResponse
from App1.backends import *

# Create your views here.
def index(request):
    if request.method=="POST":
        print(request.POST)
        name=request.POST.get('fname')
        email=request.POST.get('email')
        people=request.POST.get('people')
        price=request.POST.get('price')
        customer=Customer(name = name, email = email, people = people, price = price)
        customer.save()
        return render(request,'success.html')
    return render(request,'index.html')

@csrf_exempt
def addBuyer(request):
    try:
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password') 
        addBuyer = Buyer.objects.create_user(username = email, email = email,  password = password)
        addBuyer.save()
        return JsonResponse({"msg":"Buyer added successfully"})
    except Exception as e:
        return JsonResponse({"msg":str(e)})

@csrf_exempt
def buyerLogin(request):
    try:
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        buyer = BuyerBackend().authenticate(request, username=email, password=password)
        print(buyer)
        if buyer is not None:
            buyer.backend = 'django.contrib.auth.backends.ModelBackend'
            auth_login(request, buyer)
            return JsonResponse({"msg": "Buyer Login Successful"})
        else:
            return JsonResponse({"msg":"Please Enter Correct password or email"})

    except Exception as e:
        return JsonResponse({"msg":str(e)})