from django.urls import path 

from .views import (
    ManagementStaffListAPIView,
    ManagementStaffRetrievePIView,
)

urlpatterns = [ 
    path('management-staff/', ManagementStaffListAPIView.as_view()),
    path('management-staff/<int:pk>/', ManagementStaffRetrievePIView.as_view()),
]  
