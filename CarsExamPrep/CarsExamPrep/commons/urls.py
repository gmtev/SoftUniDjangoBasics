from django.urls import path
from CarsExamPrep.commons.views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]