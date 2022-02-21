# Local imports
from apps.media.models import Media, ArticleWp

cross_definition_dict = [
    {'field': [Media.id, ArticleWp.ID]},
    {'field': [Media.file, ArticleWp.post_mime_type]},
    {'field': [Media.name, ArticleWp.guid]},
    {'field': [Media.created_at, ArticleWp.post_date]},
    {'field': [Media.created_at, ArticleWp.post_date_gmt]},
    {'field': [Media.updated_at, ArticleWp.post_modified]},
    {'field': [Media.updated_at, ArticleWp.post_modified_gmt]}
]
