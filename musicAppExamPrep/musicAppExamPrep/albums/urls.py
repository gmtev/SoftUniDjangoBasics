from django.urls import path, include
from musicAppExamPrep.albums.views import AlbumCreateView, AlbumEditView, AlbumDetailsView, AlbumDeleteView

urlpatterns = [
    path('add/', AlbumCreateView.as_view(), name='album-add'),
    path('<int:id>/', include([
        path('edit/', AlbumEditView.as_view(), name='album-edit'),
        path('details/', AlbumDetailsView.as_view(), name='album-details'),
        path('delete/', AlbumDeleteView.as_view(), name='album-delete'),
    ]))
]