
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='注册页面'),
    path('login/', views.login, name='登录页面'),
    path('logout/', views.logout, name='退出页面'),

]
