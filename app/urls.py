from django.urls import path

from app import views

urlpatterns = [
    path('jobs/', views.job_list),
    path('jobs/<int:pk>/', views.job_detail)
]