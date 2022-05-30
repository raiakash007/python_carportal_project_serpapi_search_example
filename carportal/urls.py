"""carportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from carportalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homemethod),
    path('welcomepage/', views.hello),
    path('index/', views.indexmethod),
    path('cars/',views.carsmethod),
    path('contactus/',views.contactusmethod),
    path('contactusshow/',views.contactusrender),
    path('userlogin/',views.userlogin),
    path('userloginprocess/',views.userloginmethod),#user login process
    path('userdash/',views.userdashboard), #user dashboard
    path('signup/',views.signupmethod),
    path('signuprender/',views.signuprender),
    path('userlogout/',views.userlogout),
    path('adminlogin/',views.adminlogin), #admin login page render
    path('adminloginprocess/',views.adminmethod), #admin login process
    path('admindash/',views.admindashboard), #admin dashboard
    path('adminlogout/',views.adminlogout), #admin logout
    path('registeredusers/',views.registeredusers),
    path('addproduct/',views.addProductmethod),
    path('productrender/',views.addproductrender),
    path('addproductbycustomer/',views.addProductbycustomermethod),
    path('productrenderbycustomer/',views.addproductrenderbycustomer),
    path('product_listing/',views.productlisting),
    path('cardetails/',views.cardetailmethod),
    path('servicecenter/',views.servicecentermethod),
    path('serviceprocess/',views.serviceprocess)
    
   ]
