from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectView.as_view()),
    path('projects/details/', views.ProjectDetailView.as_view()),
    path('weeklyreport/', views.ProjectWeeklyReportView.as_view()),
    path('allweeklyreport/', views.AllWeeklyReportView.as_view()),
    path('projectstatus/', views.ProjectStatusView.as_view()),
    path('timeline/', views.PhaseWiseTimelineView.as_view()),
    path('timeline/phase/', views.PhaseView.as_view()),
    path('tasktodo/', views.TaskToDoView.as_view()),
    path('accomplishments/', views.AccomplishmentView.as_view()),
    path('risk/', views.RiskView.as_view()),
    path('issue/', views.IssueView.as_view()),
    path('assumptions/', views.AssumptionView.as_view()),
    path('dependancy/', views.DependencyView.as_view()),
]
