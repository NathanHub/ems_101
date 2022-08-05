from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('employee_detail/<int:id>/', views.employee_detail, name='employee_detail'),
]
