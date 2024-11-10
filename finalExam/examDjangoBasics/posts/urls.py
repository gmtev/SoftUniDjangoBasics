from django.urls import path, include
from examDjangoBasics.posts import views

urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name='create-post'),
    path('<int:id>/', include([
        path('edit/', views.PostEditView.as_view(), name='edit-post'),
        path('details/', views.PostDetailsView.as_view(), name='details-post'),
        path('delete/', views.PostDeleteView.as_view(), name='delete-post'),
    ]))]
