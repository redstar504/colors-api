from django.urls import path

from app import views

urlpatterns = [
    path('colors/', views.color_list),
    path('colors/<int:pk>/', views.color_detail)
]