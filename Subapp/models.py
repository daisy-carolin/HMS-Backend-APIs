from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, phone_number, password=None):
        if not email:
            raise ValueError("Email is required.")
        if not phone_number:
            raise ValueError("Phone number is required.")

        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)  # Adjust max_length as needed

   
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    def __str__(self):
        return self.email


    def create_superuser(self, email, phone_number, password=None):
        user = self.create_user(email=email, phone_number=phone_number, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class UserRegistration(AbstractBaseUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = UserManager()

    def __str__(self):
        return self.email

class UserLoginManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Email is required.")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

class UserLogin(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserLoginManager()

    def __str__(self):
        return self.email

class ListOfHotels(models.Model):
    hotel_name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)

    def __str__(self):
        return self.location   

class Reservation(models.Model):
    queue=models.CharField(max_length=50)
    allocation=models.CharField(max_length=50)
    number_of_guest=models.CharField(max_length=250)
    date=models.DateTimeField()
    time=models.TimeField()

    def __str__(self):
        return self.number_of_guest   

class DineIn(models.Model):
    qr_code=models.CharField(max_length=250)

    def __str__(self):
        return self.qr_code   

class OrderQuantity(models.Model):
    order_number = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)
    item = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number    
    
class Payments(models.Model):
    payment_method = models.CharField(max_length=250)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    transanction_id=models.CharField(max_length=50,null=True,blank=True)
   
    def __str__(self):
        return f"Payment #{self.id}"

