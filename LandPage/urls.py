from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('gallery', views.gallery, name='gallery'),
    path('confirmation', views.confirmation, name='confirmation'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('test', views.test, name='test'),
    path('logout', views.logout, name='logout'),
    path('activateAccount', views.activateAccount, name='activateAccount'),
    path('news', views.news, name='news'),
    path('forgotPassword', views.forgotPassword, name='forgotPassword'),
    path('accountRecover', views.accountRecover, name='accountRecover'),
    path('changePass', views.changePass, name='changePass'),
    path('subscribe', views.subscribe, name='subscribe'),
]