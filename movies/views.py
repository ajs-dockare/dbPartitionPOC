from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Movie, Organisation
from .permissions import IsOwnerOrReadOnly
from .serializers import MovieSerializer, OrganizationSerializer
from .pagination import CustomPagination
from .filters import MovieFilter
from django.db import connection


class ListCreateOrganisationView(ListCreateAPIView):
    serializer_class = OrganizationSerializer
    queryset = Organisation.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        obj = serializer.save()
        cursor = connection.cursor()
        tstring = 'CREATE TABLE movies_movie_{} PARTITION OF movies_movie FOR VALUES IN ({})'.format(obj.id, obj.id)
        cursor.execute(tstring)
        cursor.close()
        connection.close()


class ListCreateMovieAPIView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MovieFilter

    def perform_create(self, serializer):
        # Assign the user who created the movie
        serializer.save(creator=self.request.user)


class RetrieveUpdateDestroyMovieAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]





