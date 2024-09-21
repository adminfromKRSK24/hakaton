from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.my_view, name='my_view'),
    path('event/', views.get_post_event, name='get_post_event'),
    path('calendar/', views.show_calendar, name='show_calendar'),
    
]

