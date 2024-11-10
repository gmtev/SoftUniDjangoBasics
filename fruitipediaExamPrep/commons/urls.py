from django.urls import path
from commons.views import DashboardView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),]