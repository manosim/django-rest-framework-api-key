import uuid
from django.db import models
import re


class APIKey(models.Model):

    class Meta:
        verbose_name_plural = "API Keys"
        ordering = ['-created']

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=50, unique=True)
    key = models.CharField(max_length=40, unique=True)
    path_re = models.CharField(max_length=1024) # an RE that this api-key is validate for

    def __str__(self):
        return self.name

    def is_valid(self, path):
        pattern = re.compile(self.path_re)
        return pattern.search(path)
