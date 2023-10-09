from django.urls import path
from . import views

urlpatterns = [
    path('risk/', views.RiskView.as_view()),
    path('issue/', views.IssueView.as_view()),
]