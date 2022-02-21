from apps.sections.models import Sections


def get_all_items_by_supplement_id(
        supplement_id: int
):
    return Sections.objects.using('source').filter(
        supplement_id=supplement_id
    )


def get_list_ids_by_supplement_id(
        supplement_id: int
):
    print(supplement_id)
    return list(Sections.objects.using('source').filter(
        supplement_id=supplement_id
    ).values_list('id', flat=True).distinct())


def get_all_sections():
    return Sections.objects.using('source').all()
