from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('addrecipe', views.addrecipe, name='addrecipe'),
]

