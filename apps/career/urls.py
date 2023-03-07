from django.urls import path 

from .views import (
    VacancyListAPIView, 
    VacancyRetrieveAPIView, 
    VacancyResumeCreateAPIView,
    ResumeCreateAPIView,
    VolunteerCreateAPIView
)

urlpatterns = [ 
    path('vacancy-list/', VacancyListAPIView.as_view()),
    path('vacancy/<int:pk>/', VacancyRetrieveAPIView.as_view()),
    path('create-vacancy-resume/', VacancyResumeCreateAPIView.as_view()),
    path('create-resume/', ResumeCreateAPIView.as_view()),
    path('create-volunteer/', VolunteerCreateAPIView.as_view()),
]  
