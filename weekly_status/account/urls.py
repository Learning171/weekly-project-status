from django.urls import path, include
from account.views import (
    UserRegistartionView,
    UserLoginView,
    UserProfileView,
    UserProfileIdView,
    UserChangePasswordView,
    SendPasswordResetEmailView,
    UserPasswordResetView,
    UserLogoutView,
    AdminUserListView,
    ManagementUserListView,
    ProjectManagerUserListView,
)

urlpatterns = [
    path("register/", UserRegistartionView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("profile/<int:pk>/", UserProfileView.as_view(), name="profile"),
    path("profileid/<int:pk>/", UserProfileIdView.as_view(), name="profile"),
    path("adminlist/", AdminUserListView.as_view(), name="adminlist"),
    path("managementlist/", ManagementUserListView.as_view(), name="managementlist"),
    path(
        "projectmanagerlist/",
        ProjectManagerUserListView.as_view(),
        name="projectmanagerlist",
    ),
    path("changepassword/", UserChangePasswordView.as_view(), name="changepassword"),
    path(
        "send-reset-password-email/",
        SendPasswordResetEmailView.as_view(),
        name="send-reset-password-email",
    ),
    path(
        "reset-password/<uid>/<token>/",
        UserPasswordResetView.as_view(),
        name="reset-password",
    ),
]
