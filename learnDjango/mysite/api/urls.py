from django.urls import path
from . import views

urlpatterns = [
    path("student/", views.StudentCreate.as_view(), 
    name="blogpost-view-create "),
    path("student/<int:pk>/", views.StudentUpdateDestroy.as_view(), name="update")
]
