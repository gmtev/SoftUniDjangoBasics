from django.urls import path
from musicAppExamPrep.profiles import views
from musicAppExamPrep.profiles.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('profile/details/', views.ProfileDetailView.as_view(), name='profile-details'),
    path('profile/delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
]