from apps.supplements.selectors import get_supplements_list


supplement_list = get_supplements_list()

SUPPLEMENT_LIST = []

for supplement in supplement_list:
    SUPPLEMENT_LIST.append(
        (supplement.id, supplement.name)
    )