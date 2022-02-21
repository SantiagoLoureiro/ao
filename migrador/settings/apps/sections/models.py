from django.db import models


class Sections(models.Model):
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


class ArticleWp(models.Model):
    ID = models.AutoField(primary_key=True)
    post_author = models.IntegerField(null=True, default=1)
    post_date = models.DateTimeField(null=True)
    post_date_gmt = models.DateTimeField(null=True)
    post_content = models.TextField(null=False)
    post_title = models.TextField(null=True)
    post_excerpt = models.TextField(null=True, default='no field')
    post_status = models.TextField(null=True, default='publish')
    comment_status = models.TextField(null=True, default='closed')
    ping_status = models.TextField(null=True, default='open')
    post_password = models.TextField(null=True, default='')
    post_name = models.TextField(null=True)
    to_ping = models.TextField(null=True, default='1')
    pinged = models.TextField(null=True, default='1')
    post_modified = models.DateTimeField(null=True)
    post_modified_gmt = models.DateTimeField(null=True)
    post_content_filtered = models.TextField(null=True, default='')
    post_parent = models.IntegerField(null=False, default=0)
    guid = models.TextField(null=True, default='0')
    menu_order = models.IntegerField(null=True, default=0)
    post_type = models.TextField(null=True, default='page')
    post_mime_type = models.TextField(null=True, default='html')
    comment_count = models.IntegerField(null=True, default=0)

    class Meta:
        db_table = "wp_posts"
        managed = False

    def set_guid(self):
        self.guid = f'~/wordpress/?page_id={self.ID}'

    def set_post_name(self):
        lower_post_name = self.post_title.lower()
        self.post_name = lower_post_name.replace(' ', '-')

    def play_with_my_fields(self, object_source=None):
        self.set_post_name()

    def fix_details_post_save(self, object_source=None):
        self.set_guid()
        self.save()
