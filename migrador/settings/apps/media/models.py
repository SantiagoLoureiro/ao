from django.db import models


class Media(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.TextField(null=True)
    file = models.TextField(null=True)
    content = models.TextField(null=True)
    small_version = models.TextField(null=True)
    medium_version = models.TextField(null=True)
    big_version = models.TextField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    name = models.TextField(null=True)
    date = models.DateTimeField(null=True)
    credits = models.TextField(null=True)
    dimensions = models.TextField(null=True)
    xbig_version = models.TextField(null=True)
    xsmall_version = models.TextField(null=True)

    class Meta:
        db_table = "media"
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
    post_status = models.TextField(null=True, default='inherit')
    comment_status = models.TextField(null=True, default='closed')
    ping_status = models.TextField(null=True, default='closed')
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
    post_type = models.TextField(null=True, default='attachment')
    post_mime_type = models.TextField(null=True, default='html')
    comment_count = models.IntegerField(null=True, default=0)

    class Meta:
        db_table = "wp_posts"
        managed = False

    def set_guid(self):
        self.guid = f'~/wordpress/wp-content/uploads/migracion/{self.guid}'

    def transform_post_mime_type(self):
        mime_type = self.post_mime_type.split('.')[-1]
        if mime_type == '.pdf':
            self.post_mime_type = 'application/pdf'
        if mime_type in ['jpg', 'JPG']:
            self.post_mime_type = 'image/jpg'
        if mime_type in ['mp3', 'MP3']:
            pass

    def play_with_my_fields(self, object_source=None):
        self.transform_post_mime_type()
        self.set_guid()

