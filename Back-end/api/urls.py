from django.urls import path, include
from django.conf.urls import url
from api import views


urlpatterns = [
	path('register/', views.register, name = "register"),
]