from django.urls import path, include
from fruits.views import (
    FruitCreateView, FruitDetailsView, FruitEditView, FruitDeleteView
)

urlpatterns = [
    path('create/', FruitCreateView.as_view(), name='create-fruit'),
    path('<int:id>/', include([
        path('edit/', FruitEditView.as_view(), name='edit-fruit'),
        path('details/', FruitDetailsView.as_view(), name='details-fruit'),
        path('delete/', FruitDeleteView.as_view(), name='delete-fruit'),
    ]))]

