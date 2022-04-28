import uuid
from django.db import models

class Courier(models.Model):
    '''This model is included couriers' details'''
    full_name = models.CharField(max_length=220)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.full_name