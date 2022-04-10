from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('do_or_do_not/', views.do_or_do_not, name='do_or_do_not'),
    path('going_for_email/', views.going_for_email, name='going_for_email'),

    path('set_cookie/', views.set_cookie, name='set_cookie'),





    path('connect_massage_send/', views.connect_massage_send, name='connect_massage_send'),


]