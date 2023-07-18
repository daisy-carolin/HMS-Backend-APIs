
from rest_framework import serializers, fields
from Subapp.models import UserRegistration,UserLogin,ListOfHotels,Reservation,DineIn,OrderQuantity,Payments
from .models import *


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ("phone_number","email", "password", )


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = ("email", "password", )

class ListOfHotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListOfHotels
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"


class DineInSerializer(serializers.ModelSerializer):
    class Meta:
        model = DineIn
        fields = "__all__"


class OrderQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderQuantity
        fields = "__all__"


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"