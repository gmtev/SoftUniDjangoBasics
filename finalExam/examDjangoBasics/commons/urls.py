from django.urls import path
from examDjangoBasics.commons import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
]
