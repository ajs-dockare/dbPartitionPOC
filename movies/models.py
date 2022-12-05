from django.db import models
from django.utils.translation import gettext_lazy as _
from psqlextra.types import PostgresPartitioningMethod
from psqlextra.models import PostgresPartitionedModel


class Organisation(models.Model):
    objects = models.Manager()
    id = models.AutoField(
        _("Unique identifier for Organisation"),
        primary_key=True,
        editable=False,
    )
    name = models.CharField(max_length=150, unique=True)


class Movie(PostgresPartitionedModel):
    class PartitioningMeta:
        method = PostgresPartitioningMethod.LIST
        key = ["organisation_id"]

    id = models.AutoField(
        primary_key=True,
        editable=False,
    )
    title = models.CharField(max_length=100)
    organisation = models.ForeignKey(
        Organisation,
        null=True,
        on_delete=models.DO_NOTHING,
        unique=False,
    )
    # organisation_id = models.IntegerField()
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)

    REQUIRED_FIELDS = [
        "title",
        "genre",
        "year",
        "organisation_id",
    ]


# Following is a regular "Movie" model
# class Movie(models.Model):
#     title = models.CharField(max_length=100)
#     genre = models.CharField(max_length=100)
#     year = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     creator = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)
#
#     class Meta:
#         ordering = ['-id']

