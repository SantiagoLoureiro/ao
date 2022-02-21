from django.db import models


class Supplements(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(null=True)
    is_default = models.IntegerField()
    created_at = models.TextField(null=True)
    updated_at = models.TextField(null=True)
    active_edition_id = models.IntegerField()
    logo_id = models.IntegerField()
    news_source_id = models.IntegerField()

    class Meta:
        db_table = "supplements"
        managed = False

