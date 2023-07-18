from django.shortcuts import render
from django.shortcuts import render
from Subapp.models import *

# Create your views here.

from datetime import datetime
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response

from .models import UserRegistration,UserLogin,ListOfHotels,Reservation,DineIn,OrderQuantity,Payments
from .serializers import (
UserRegistration,
UserLogin,
ListOfHotels,
Reservation,
DineIn,
OrderQuantity,
Payments,

   )

from drf_yasg.utils import swagger_auto_schema


from .serializers import *

from django.contrib.auth.hashers import make_password
from Subapp.serializers import ListOfHotelsSerializer

# Create your views here.

class UserRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegistrationSerializer

    @swagger_auto_schema(responses={200: UserRegistrationSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        user_registration= UserRegistration.objects.all()
        serializer = UserRegistrationSerializer( user_registration, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=UserRegistrationSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = UserRegistrationSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer

    @swagger_auto_schema(responses={200: UserLoginSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        user_login= UserLogin.objects.all()
        serializer = UserLoginSerializer( user_login, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=UserLoginSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = UserLoginSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ListOfHotelsView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ListOfHotelsSerializer

    @swagger_auto_schema(responses={200: ListOfHotelsSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        list_of_hotels= ListOfHotels.objects.all()
        serializer = ListOfHotelsSerializer( list_of_hotels, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=ListOfHotelsSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = ListOfHotelsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ReservationView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ReservationSerializer

    @swagger_auto_schema(responses={200: ReservationSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        reservation= Reservation.objects.all()
        serializer = ReservationSerializer(reservation, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=ReservationSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = ReservationSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class DineInView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = DineInSerializer

    @swagger_auto_schema(responses={200: DineInSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        dine_in= DineIn.objects.all()
        serializer = DineInSerializer(dine_in, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=DineInSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = DineInSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        

class OrderQuantityView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderQuantitySerializer

    @swagger_auto_schema(responses={200: OrderQuantitySerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        order_quantity= OrderQuantity.objects.all()
        serializer = OrderQuantitySerializer(order_quantity, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=OrderQuantitySerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = OrderQuantitySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        

class PaymentsView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PaymentsSerializer

    @swagger_auto_schema(responses={200: PaymentsSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        payments= Payments.objects.all()
        serializer = PaymentsSerializer(payments, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=PaymentsSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = PaymentsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)