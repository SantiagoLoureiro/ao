from apps.articles.models import Article, ArticleWp


def get_all_items_by_section_id_list(
    section_id_list
):

    return Article.objects.using('source').filter(
        section_id__in=section_id_list
    )


def get_item_by_id(
        id: str
):

    return ArticleWp.objects.using('destination').get(ID=id)
