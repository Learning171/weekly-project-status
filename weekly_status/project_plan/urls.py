from django import views
from django.urls import path
from .views import WeeklyReportView,WeeklyReportID,TaskToDoView,AccomplishmentView

urlpatterns = [
    # WeeklyReport urls
    path('WeekReportID/<int:id>/',WeeklyReportID.as_view()),
    path('WeekReportAll/',WeeklyReportView.as_view()),
    path('WeekReportAll/id/<int:id>/update/', WeeklyReportView.as_view()),
    path('WeekReportAll/delete/<int:id>/', WeeklyReportView.as_view()),
    # # ToDo urls
    path('TaskToDo/', TaskToDoView.as_view()),
    path('TaskToDo/update/<int:id>/', TaskToDoView.as_view()),
    path('TaskToDo/delete/<int:id>/', TaskToDoView.as_view()),
    # # Accomplishment urls
    path('Accomp/',AccomplishmentView.as_view()),
    path('Accomp/update/<int:id>/', AccomplishmentView.as_view()),
    path('Accomp/delete/<int:id>/', AccomplishmentView.as_view()),
 
]
