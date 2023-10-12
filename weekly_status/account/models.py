# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# class UserManager(BaseUserManager):
#     def create_user(self, user_email, user_name, user_type, password=None, password2=None):
#         """Creates and saves a User with the given user_email, user_name, user_type, and password."""
#         if not user_email:
#             raise ValueError("User must have an email address")
			
#         user = self.model(
#             user_email=self.normalize_email(user_email),
#             user_name=user_name,
#             user_type=user_type,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, user_email, user_name, user_type, password=None):
#         """Creates and saves a superuser with the given email, name, user_type, and password."""
#         user = self.create_user(user_email, user_name=user_name, user_type=user_type, password=password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user

# class User(AbstractBaseUser, PermissionsMixin):
#     user_email = models.EmailField(
#         verbose_name="Email",
#         max_length=255,
#         unique=True,
#     )
#     user_name = models.CharField(max_length=200)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     user_choice = (("Admin", "Admin"), ("Project_manager", "Project Manager"), ("Management", "Management"),)
#     user_type = models.CharField(max_length=20, choices=user_choice)

#     objects = UserManager()

#     USERNAME_FIELD = "user_email"
#     REQUIRED_FIELDS = ["user_name", "user_type"]

#     def __str__(self):
#         return self.user_email

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, user_email, user_name, user_type, password=None, password2=None):
        if not user_email:
            raise ValueError("User must have an email address")

        user = self.model(
            user_email=self.normalize_email(user_email),
            user_name=user_name,
            user_type=user_type,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_email, user_name, user_type, password=None):
        user = self.create_user(user_email, user_name=user_name, user_type=user_type, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    user_email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    user_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_choice = (
        ("Admin", "Admin"),
        ("Project_manager", "Project Manager"),
        ("Management", "Management"),
    )
    user_type = models.CharField(max_length=20, choices=user_choice)

    objects = UserManager()

    USERNAME_FIELD = "user_email"
    REQUIRED_FIELDS = ["user_name", "user_type"]

    def __str__(self):
        return self.user_email