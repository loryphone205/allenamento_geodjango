from django.urls import path
from .views import PointOfInterestDetail, PointOfInterestListCreate, index

urlpatterns = [
    path('pois/', PointOfInterestListCreate.as_view(), name='poi-list-create'),
    path('pois/<int:pk>/', PointOfInterestDetail.as_view(), name='poi-detail'),
    path('', index)
]

