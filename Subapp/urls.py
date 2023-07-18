from django.urls import path
from . import views
#create your urls here
#api urls   
urlpatterns = [
path('user_regstration', views.UserRegistrationView.as_view(),name='user_regstration_api'),
path('user_login', views.UserLoginView.as_view(),name='user_login_api'),
path('list_of_hotels', views.ListOfHotelsView.as_view(),name='list_of_hotels_api'),
path('reservation', views.ReservationView.as_view(),name='reservation_api'),
path('dine_in', views.DineInView.as_view(),name='dine_in_api'),
path('order_quantity', views.OrderQuantityView.as_view(),name='order_quantity_api'),
path('payments', views.PaymentsView.as_view(),name='payments_api'),

]