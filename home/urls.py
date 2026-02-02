from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
]