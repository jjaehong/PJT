from django.urls import path
from . import views

urlpatterns = [
    path('normal_sort/', views.normal_sort),
    path('priority_queue/', views.priority_queue),
    path('bubble_sort/', views.bubble_sort),
    path('savedata/', views.savedata),
    path('savenulldata/', views.savenulldata),
    path('avg_age/',views.avg_age),
]
    


