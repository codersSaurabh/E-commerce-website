from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('', views.index,name="shopHome"),
    path('about/', views.about,name="AboutUs"),
    path('contact/', views.contact,name="ContactUs"),
    path('tracker/', views.tracker,name="TrackingStauts"),
    path('product/<int:prid>', views.productview,name="ProductView"),
    path('search/', views.search,name="search"),
    path('checkout/', views.checkout,name="Checkout"),
]
