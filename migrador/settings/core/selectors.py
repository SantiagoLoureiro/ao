from core.models import RealtionIdSourceDestination


def createRelationSourceDestinationObject(
        operation: int,
        source_object,
        destionation_object
):
    try:
        source_id = source_object.id
    except:
        source_id = source_object.ID

    try:
        destination_id = destionation_object.id
    except:
        try:
            destination_id = destionation_object.ID
        except:
            destination_id = destionation_object.term_id

    relation = RealtionIdSourceDestination(
        operation=operation,
        source_id=source_id,
        destination_id=destination_id
    )
    relation.save()


def get_destination_id_by_source_id_and_operation(
        operation,
        source_id
):
    return RealtionIdSourceDestination.objects.using('default').filter(
        operation=operation,
        source_id=source_id
    ).first()


def clean_default_db():
    queryset = RealtionIdSourceDestination.objects.using('default').all()
    for x in queryset:
        x.delete()
