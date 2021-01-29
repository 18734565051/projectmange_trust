from . import views
from django.urls import path

urlpatterns = [
    path('File/', views.Approval_File.as_view()),
]
