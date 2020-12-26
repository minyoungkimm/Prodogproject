from django.urls import path
from . import views

urlpatterns = [
    path("main/", views.main, name="main"),
    path('register/', views.register, name="register"),
    path('newLogin/', views.newLogin, name="newLogin"),
    path('sign_in/', views.sign_in, name="sign_in"),
    path('main_onlyMember/', views.main_onlyMember, name="main_onlyMember"),
]