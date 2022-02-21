from apps.supplements.models import Supplements


def get_supplements_list():
    return Supplements.objects.using('source').all()