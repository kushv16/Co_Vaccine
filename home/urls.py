from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('appointment',views.appointment,name='appointment'),
    path('faq',views.faq,name='faq'),

]