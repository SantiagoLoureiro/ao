# Local imports
from apps.articles.models import Article, ArticleWp

cross_definition_dict = [
    {'field': [Article.id, ArticleWp.ID]},
    {'field': [Article.heading, ArticleWp.post_content]},
    {'field': [Article.lead, ArticleWp.post_excerpt]},
    {'field': [Article.body, ArticleWp.post_content]},
    {'field': [Article.title, ArticleWp.post_title]},
    {'field': [Article.slug, ArticleWp.post_name]},
    {'field': [Article.created_at, ArticleWp.post_date]},
    {'field': [Article.created_at, ArticleWp.post_date_gmt]},
    {'field': [Article.updated_at, ArticleWp.post_modified]},
    {'field': [Article.updated_at, ArticleWp.post_modified_gmt]}
]


