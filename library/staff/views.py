from rest_framework.viewsets import ModelViewSet

from .models import Staff
from .serializers import StaffSerializer

class StaffViewSet(ModelViewSet):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()

