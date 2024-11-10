from django.contrib import admin
from django.urls import path, include
from commons.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),  # Index page
    path('dashboard/', include('commons.urls')),  # Dashboard
    path('fruit/', include('fruits.urls')),  # Fruit-related URLs
    path('profile/', include('profiles.urls')),  # Profile-related URLs
]
