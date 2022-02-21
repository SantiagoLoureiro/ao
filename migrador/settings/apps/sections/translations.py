from core.selectors import get_destination_id_by_source_id_and_operation
from core.constants import Operation


class Translator(object):

    @staticmethod
    def none_effect(**kwargs):
        return kwargs['attr']

    @staticmethod
    def attribute_parent_id(**kwargs):
        # relation = get_destination_id_by_source_id_and_operation(
        #    operation=Operation.ARTICLES.value,
        #    source_id=kwargs['attr']
        #)
        # return relation.destination_id

        if kwargs['attr'] == None:
            return 1
        return kwargs['attr']
