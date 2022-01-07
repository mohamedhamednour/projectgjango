from  django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views  as Authentication
from userApp import views
urlpatterns = [
    # path('', views.home),
    path('signup', views.signup, name='sign'),
    path('logout',views.logOut , name='logout'),
    path('viewuser',views.viewuser,name='viewUser'),
    path('userProfileView',views.userProfileView,name='userProfileView'),
    path('login',views.loginbase ,name='login'),
    path('',Authentication.LoginView.as_view(template_name='demo/login.html'),name='log'),
    path('settings/passwors/',Authentication.PasswordChangeView.as_view(template_name='demo/chanche.html'),name='chan')

]