from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.home),
	path('about/', views.about)
	# basic pages
	path('home1/', views.home),
	path('about1/', views.about1),
	path('contact/', views.contact),
	path('services/', views.services),
	# dyanamic URL
	path('welcome/<str:>/', views.welcome)
]