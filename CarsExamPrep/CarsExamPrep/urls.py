from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CarsExamPrep.commons.urls')),
    path('car/', include('CarsExamPrep.cars.urls')),
    path('profile/', include('CarsExamPrep.profiles.urls')),
]