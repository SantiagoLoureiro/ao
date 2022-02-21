from django.db import models


class RealtionIdSourceDestination(models.Model):
    id = models.IntegerField(primary_key=True)
    operation = models.TextField(null=True, default='operation')
    source_id = models.IntegerField(null=True, default=1)
    destination_id = models.IntegerField(null=True, default=1)
