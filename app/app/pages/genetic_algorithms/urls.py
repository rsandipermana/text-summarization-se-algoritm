from django.urls import path
from . import views

urlpatterns = [
    path('summarize/', views.summarize),
    path('<int:pk>/', views.detail),
]