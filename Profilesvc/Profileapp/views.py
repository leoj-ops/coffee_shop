from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import *
from rest_framework import permissions
from .models import *
from json import JSONDecodeError
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from django.core import serializers
from django.http import HttpResponse
import json
import traceback

# Create your views here.

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def profile(request):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        try:
            email_id = request.data.get("email_id")
            print(email_id,"\n\n********************")
            profile = Profile.objects.get(email_id=email_id)
            customer_id = profile.customer_id
            loyalty_point = profile.loyalty_point
            return Response({'error': 'Email ID already exists','customer_id':customer_id,'loyalty_point':loyalty_point})
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def loyalty(request,customer_id):
    try:
        profile = Profile.objects.get(customer_id=customer_id)
        loyalty_point = profile.loyalty_point
        email_id = profile.email_id
        return Response({'loyalty_point':loyalty_point,'email_id':email_id})
    except:
        return Response("Errors no user found", status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def checkout(request):
    try:
        customer_id = request.data.get("customer_id")
        item = request.data.get("item")
        price_paid = request.data.get("price_paid")
        profile = Profile.objects.get(customer_id=customer_id)
        loyalty_point = profile.loyalty_point
        print("***************\n",loyalty_point,"\n***************\n")
        if(loyalty_point%4==0):
            price_paid = 0.0
        transaction = Transaction(customer_id=profile, item=item, price_paid=price_paid)
        transaction.save()
        profile.loyalty_point = profile.loyalty_point + 1
        profile.save()


        return Response({"message": "Transaction created successfully.",'price paid': price_paid})
    except Exception as e:
        traceback.print_exc()
        return Response({"error": "Failed to create transaction."}, status=status.HTTP_400_BAD_REQUEST)
        
