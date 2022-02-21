# Django importsdestination_model
from django.db import models

# Python imports
from typing import Dict

# Local imports
from core.selectors import createRelationSourceDestinationObject
from apps.articles.models import ArticleWp
from apps.section.models import TermWp


def __init__(
        self,
        destination_model,
        source_obj,
        dict_ref: Dict,
):
    self.source_obj = source_obj
    self.destination_model = destination_model
    self.dict_ref = dict_ref


class MigrantCore(object):

    def __init__(
        self,
        list_cross,
        destination_model,
        list_objects,
        operation
    ):
        self.list_cross = list_cross
        self.destination_model = destination_model
        self.list_objects = list_objects
        self.operation = operation

    def migrate(self):
        for item in self.list_objects:
            object_destination = self.destination_model()
            for field_row in self.list_cross:
                parameters = {'attr': getattr(item, field_row['field'][0])}
                if 'parameters' in field_row:
                    parameters.update(field_row['parameters'])
                attr_result = field_row['function'](**parameters)
                setattr(object_destination, field_row['field'][1], attr_result)
            try:
                object_destination.play_with_my_fields(object_source=item)

                if self.destination_model == ArticleWp:
                    object_destination.ID += 5000
                    object_destination.save(using='destination')
                elif self.destination_model == TermWp:
                    object_destination.term_id += 5000
                    object_destination.save(using='destination')
                else:
                    object_destination.save(using='destination')


                try:
                    object_destination.fix_details_post_save(object_source=item)
                except:
                    pass

                createRelationSourceDestinationObject(
                    operation=self.operation,
                    source_object=item,
                    destionation_object=object_destination
                )

            except Exception as error:
                print(error)
