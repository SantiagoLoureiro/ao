from django.db import models


class Section(models.Model):
    created_at = models.DateTimeField(null=True)
    id = models.IntegerField(primary_key=True)
    is_visible = models.IntegerField(null=True)
    main_article_id = models.IntegerField(null=True)
    name = models.TextField(null=True)
    parent_id = models.IntegerField(null=True)
    slug = models.TextField(null=True)
    supplement_id = models.IntegerField(null=True)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        db_table = "sections"
        managed = False


class TermWp(models.Model):
    term_id = models.AutoField(primary_key = True)
    name = models.TextField(null=False)
    slug = models.TextField(null=False)

    class Meta:
        db_table = "wp_terms"
        managed = False

    def create_slug(self):
        slug = self.name.lower()
        self.slug = slug.replace(' ', '-')

    def play_with_my_fields(self, object_source=None):
        self.create_slug()

    def fix_details_post_save(self, object_source=None):
        pass
