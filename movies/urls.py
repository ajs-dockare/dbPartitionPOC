from django.urls import path
from . import views


urlpatterns = [
    path('orgs', views.ListCreateOrganisationView.as_view(), name='get_post_organisations'),
    path('', views.ListCreateMovieAPIView.as_view(), name='get_post_movies'),
    path('<int:pk>/', views.RetrieveUpdateDestroyMovieAPIView.as_view(), name='get_delete_update_movie'),
]