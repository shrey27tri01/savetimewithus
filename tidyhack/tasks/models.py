from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# from cassandra.cqlengine import columns
# from django_cassandra_engine.models import DjangoCassandraModel


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=30)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    completed_picture = models.ImageField(upload_to='media',blank=True)


    class Meta:
        ordering = ('created',)

    def __str__(self) -> str:
        return self.title