from django.urls import path
from students import views

urlpatterns = [
    path('student', views.StudentListCreate.as_view()),
]
