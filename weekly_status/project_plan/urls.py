from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectView.as_view()),
    path('projects/details/<int:pk>/', views.ProjectDetailView.as_view()),
    path('weeklyreport/<int:pk>/', views.ProjectWeeklyReportView.as_view()),
    path('weeklyreport/', views.ProjectWeeklyReportView.as_view()),
    path('allweeklyreport/', views.AllWeeklyReportView.as_view()),
    path('projectstatus/<int:pk>/', views.ProjectStatusView.as_view()),
    path('projectstatus/', views.ProjectStatusView.as_view()),
    path('timeline/<int:pk>/', views.PhaseWiseTimelineView.as_view()),
    path('timeline/', views.PhaseWiseTimelineView.as_view()),
    path('timeline/phase/<int:pk>/', views.PhaseView.as_view()),
    path('timeline/phase/', views.PhaseView.as_view()),
    path('tasktodo/<int:pk>/', views.TaskToDoView.as_view()),
    path('tasktodo/', views.TaskToDoView.as_view()),
    path('accomplishments/<int:pk>/', views.AccomplishmentView.as_view()),
    path('accomplishments/', views.AccomplishmentView.as_view()),
    path('risk/<int:pk>/', views.RiskView.as_view()),
    path('risk/', views.RiskView.as_view()),
    path('issue/<int:pk>/', views.IssueView.as_view()),
    path('issue/', views.IssueView.as_view()),
    path('assumptions/<int:pk>/', views.AssumptionView.as_view()),
    path('assumptions/', views.AssumptionView.as_view()),
    path('dependancy/<int:pk>/', views.DependencyView.as_view()),
    path('dependancy/', views.DependencyView.as_view()),
]
