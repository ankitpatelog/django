from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'employee', views.Employeeviewset, basename='employee')

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentsDetails),
    path('employee/', views.employeeDetails.as_view()),
    path('employee/<int:pk>/', views.employeeDetails.as_view()),
    path('', include(router.urls)),
    path('blogs/', views.BlogView.as_view()),
    path('comments/', views.commentView.as_view())
]