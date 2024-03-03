from django.urls import path
from app import views



urlpatterns = [
    path('home/', views.show_html, name='home'),
    path('webcam/', views.webcam2, name='webcam'),

]
 