from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView
)

from .serializers import (
    ManagementStaffSerializer,
)

from .models import Management_staff


class ManagementStaffListAPIView(ListAPIView):
    queryset = Management_staff.objects.all()
    serializer_class = ManagementStaffSerializer


class ManagementStaffRetrievePIView(RetrieveAPIView):
    queryset = Management_staff.objects.all()
    serializer_class = ManagementStaffSerializer