from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView
)

from .models import Vacancy

from .serializers import (
    VacancyListSerializer,
    VacancyRetrieveSerializer,
    VacancyResumeCreateSerializer,
    CreateResumeSerializer,
    CreateVolunteerSerializer
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


class VolunteerCreateAPIView(CreateAPIView):
    serializer_class = CreateVolunteerSerializer