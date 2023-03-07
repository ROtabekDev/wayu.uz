from django.urls import path 

from .views import ListVacancyAPIView

urlpatterns = [ 
    path('vacancy-list/', ListVacancyAPIView.as_view(), name='vacancy-list')
]  
