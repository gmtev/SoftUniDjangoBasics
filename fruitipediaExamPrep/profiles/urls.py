from django.urls import path
from profiles.views import (
    ProfileCreateView, ProfileDetailsView, ProfileEditView, ProfileDeleteView
)

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create-profile'),  # Profile create
    path('details/', ProfileDetailsView.as_view(), name='details-profile'),  # Profile details
    path('edit/', ProfileEditView.as_view(), name='edit-profile'),  # Profile edit
    path('delete/', ProfileDeleteView.as_view(), name='delete-profile'),  # Profile delete
]