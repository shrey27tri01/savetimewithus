from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel
from cqlengine import columns
from cqlengine.models import Model


# Create your models here.
class Task(models.Model):
    title = columns.Text()
    complete = columns.Boolean(default=False)
    created = columns.DateTime()   # set auto now add = True
    description = columns.Text()
    author = columns.UUID(primary_key=True)   # here we are using author id instead of django author
    completed_picture = columns.Bytes(required=False)


    class Meta:
        ordering = ('created',)

    def __str__(self) -> str:
        return self.title
