from apps.taxonomy.models import Taxonomy


def get_all_items():
    return Taxonomy.objects.using('destination').all()


def get_taxonomy_by_id(
        term_id: str
):
    return Taxonomy.objects.using('destination').filter(
        term_id=term_id
    )
