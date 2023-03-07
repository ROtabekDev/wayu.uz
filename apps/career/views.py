from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView, ListCreateAPIView
)

from .models import Vacancy, Volunteer

from .serializers import (
    VacancyListSerializer,
    VacancyRetrieveSerializer,
    VacancyResumeCreateSerializer,
    CreateResumeSerializer,
    CreateListVolunteerSerializer,
    CreateInternshipSerializer
)

class VacancyListAPIView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer


class VacancyRetrieveAPIView(RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyRetrieveSerializer


class VacancyResumeCreateAPIView(CreateAPIView):
    serializer_class = VacancyResumeCreateSerializer


class ResumeCreateAPIView(CreateAPIView):
    serializer_class = CreateResumeSerializer


class VolunteerListCreateAPIView(ListCreateAPIView):
    queryset = Volunteer.objects.all()
    serializer_class = CreateListVolunteerSerializer


class InternshipCreateAPIView(CreateAPIView):
    serializer_class = CreateInternshipSerializer