from apps.sections.models import Sections, ArticleWp

cross_definition_dict = [
    {'field': [Sections.name, ArticleWp.post_title]},
    {'field': [Sections.parent_id, ArticleWp.post_parent]},
    {'field': [Sections.created_at, ArticleWp.post_date]},
    {'field': [Sections.created_at, ArticleWp.post_date_gmt]},
    {'field': [Sections.updated_at, ArticleWp.post_modified]},
    {'field': [Sections.updated_at, ArticleWp.post_modified_gmt]}
]


