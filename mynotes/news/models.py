from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Group
from django.contrib.auth.models import UserManager

import uuid

# Create your models here.

class Article(models.Model):
    title = models.CharField("Названия ", max_length=100)
    anons = models.CharField("Анонс", max_length=250)
    full_text = models.TextField("Статья")
    date = models.DateTimeField("Дата публикации")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/news/{self.id}"

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

class LMSUser(AbstractBaseUser):
    username = models.CharField(max_length=30, null=False, unique=True)
    email = models.EmailField("email address", blank=True, unique=True)

    role = models.CharField(max_length=30, null=False, choices=[("student", "Student"), ("teacher", "Teacher")])
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING, default=None)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["password", "role", "group"]

    objects = UserManager()

    class Meta:
        verbose_name = "lms_user"
        verbose_name_plural = "lms_users"
        db_table = "first_app_lms_users"

    def __str__(self):
        return self.email