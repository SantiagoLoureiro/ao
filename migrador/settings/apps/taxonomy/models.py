from django.db import models


class Taxonomy(models.Model):
    term_taxonomy_id = models.IntegerField(primary_key=True)
    term_id = models.IntegerField(null=True, default=1)
    taxonomy = models.TextField(null=True)
    description = models.TextField(null=True)
    parent = models.IntegerField(null=True, default=0)
    count = models.IntegerField(null=True, default=1)

    class Meta:
        db_table = "wp_term_taxonomy"
        managed = False


class TermTaxonomy(models.Model):
    object_id = models.IntegerField(null=True, default=1)
    term_taxonomy_id = models.IntegerField(null=True, default=1)
    term_order = models.IntegerField(null=True, default=0)

    class Meta:
        db_table = "wp_term_relationships"
        managed = False