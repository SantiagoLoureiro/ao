

class Translator(object):

    @staticmethod
    def none_effect(**kwargs):
        return kwargs['attr']

    @staticmethod
    def attribute_post_excerpt(**kwargs):
        # relation = get_destination_id_by_source_id_and_operation(
        #    operation=Operation.ARTICLES.value,
        #    source_id=kwargs['attr']
        #)
        # return relation.destination_id
        return ''