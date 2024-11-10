from django.urls import path, include
from CarsExamPrep.cars import views

urlpatterns = [
    path('catalogue/', views.CarCatalogueView.as_view(), name='car-catalogue'),
    path('create/', views.CarCreateView.as_view(), name='car-create'),
    path('<int:id>/', include([
        path('edit/', views.CarEditView.as_view(), name='car-edit'),
        path('details/', views.CarDetailsView.as_view(), name='car-details'),
        path('delete/', views.CarDeleteView.as_view(), name='car-delete'),
    ]))
]
