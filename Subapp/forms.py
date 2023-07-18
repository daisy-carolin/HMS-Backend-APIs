from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = "__all__"


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = UserLogin
        fields = "__all__"


class ListOfHotelsForm(forms.ModelForm):
    class Meta:
        model = ListOfHotels
        fields = "__all__"


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"


class DineInForm(forms.ModelForm):
    class Meta:
        model = DineIn
        fields = "__all__"


class OrderQuantityForm(forms.ModelForm):
    class Meta:
        model = OrderQuantity
        fields = "__all__"

class PaymentsForm(forms.ModelForm):
    class Meta:
        model = Payments
        fields = "__all__"