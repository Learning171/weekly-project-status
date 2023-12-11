from project_plan import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("projectsapi", views.ProjectDetailViewSet, basename="projects")
router.register("projectslistapi", views.ProjectListViewSet, basename="projectslist")
router.register("weeklyreportapi", views.WeeklyReportViewSet, basename="weeklyreport")
router.register(
    "projectstatusapi", views.ProjectStatusViewSet, basename="projectstatus"
)
router.register(
    "phasewisetimelineapi", views.PhaseWiseTimelineViewSet, basename="phasewisetimeline"
)
router.register("phaseviewapi", views.PhaseViewSet, basename="phaseview")
router.register("tasktodoapi", views.TaskToDoViewSet, basename="tasktodo")
router.register(
    "accomplishmentsapi", views.AccomplishmentViewSet, basename="accomplishments"
)
router.register("riskapi", views.RiskViewSet, basename="risk")
router.register("issueapi", views.IssueViewSet, basename="issue")
router.register("assumptionsapi", views.AssumptionViewSet, basename="assumptions")
router.register("dependancyapi", views.DependencyViewSet, basename="dependancy")

urlpatterns = [
    path("api/projectplan/", include(router.urls)),
    path(
        "api/projectplan/projectweeklyreportapi/<int:project_id>/",
        views.ProjectWeeklyReportView.as_view(),
    ),
]
