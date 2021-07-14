from rest_framework.viewsets import ModelViewSet

from .models import Authors
from .serializers import AuthorsSerializer

class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorsSerializer
    queryset = Authors.objects.all()


