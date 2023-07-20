
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.handleRegister),
    path('login/', views.handleLogin),
    path('logout/', views.handleLogout),
    path('viewprofile/<int:user_id>/', views.viewProfile, name= 'viewprofile'),
    path('editprofile/<int:user_id>/', views.editProfile, name= 'editprofile'),
    # path('editprofile/<int:user_id>/', views.editProfile, name= 'updateprofile'),
    # path('userprofile/', views.userProfile, name= 'userprofile')
    
]