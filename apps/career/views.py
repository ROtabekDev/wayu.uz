from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView
)

from .models import Vacancy

from .serializers import (
    VacancyListSerializer
)

class ListVacancyAPIView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer