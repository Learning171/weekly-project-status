from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.ProjectView.as_view()),
    path('account/', views.AccountView.as_view()),
]
