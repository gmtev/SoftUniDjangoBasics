from django.contrib import admin
from django.urls import path, include
from examDjangoBasics.commons import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('dashboard/', include('examDjangoBasics.commons.urls')),
    path('posts/', include('examDjangoBasics.posts.urls')),
    path('author/', include('examDjangoBasics.authors.urls')),
]