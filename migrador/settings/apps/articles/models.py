from django.db import models


class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    slug = models.CharField(max_length=255)
    heading = models.TextField(null=True)
    title = models.TextField(null=True)
    lead = models.TextField(null=True)
    body = models.TextField(null=True)
    signature = models.TextField(null=True)
    section_id = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    edition_id = models.IntegerField(null=True)
    is_visible = models.IntegerField(null=True)
    hide_from_cover = models.IntegerField(null=True)
    time = models.DateTimeField(null=True)
    is_new = models.IntegerField(null=True)

    class Meta:
        db_table = "articles"
        managed = False

    def get_id(self):
        return self.id



class ArticleWp(models.Model):
    ID = models.IntegerField(primary_key=True)
    post_author = models.IntegerField(null=True, default=1)
    post_date = models.DateTimeField(null=True)
    post_date_gmt = models.DateTimeField(null=True)
    post_content = models.TextField(null=True)
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
    post_parent = models.IntegerField(null=True, default=0)
    guid = models.TextField(null=True, default='0')
    menu_order = models.IntegerField(null=True, default=0)
    post_type = models.TextField(null=True, default='post')
    post_mime_type = models.TextField(null=True, default='html')
    comment_count = models.IntegerField(null=True, default=0)

    class Meta:
        db_table = "wp_posts"
        managed = False

    def set_guid(self):
        self.guid = f'~/category_mark/{self.post_name}/{self.ID}'

    def set_post_name(self):
        self.post_name = self.post_name.replace(' ', '-')

    def play_with_my_fields(self, object_source=None):
        self.set_post_name()
        self.set_guid()


