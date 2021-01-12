from . import views
from django.urls import path

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('ProjectInfo/', views.ProjectView.as_view()),
    path('ProjectDetail/', views.ProjectDetailView.as_view()),
]
