# Local Imports
# Core

# Sections
from apps.sections import selectors as sectionSelector
from apps.articles import selectors as articleSelector

# Taxonomy
from apps.taxonomy.selectors import get_taxonomy_by_id
from apps.taxonomy.models import Taxonomy, TermTaxonomy


def migrate(
        supplement_id: int
):

    print(
        '          -----------------\n'
        '          -----------------\n'
        '          --- Articles  ---\n'
        '          -----------------\n'
        '          -----------------\n'

    )

    print(
        '       --- Generate Dictionary  ---'
    )
    list_objects = sectionSelector.get_all_items_by_supplement_id(
        supplement_id=supplement_id
    )

    for item in list_objects:
        try:
            taxonomy = Taxonomy()
            taxonomy.description = item.slug
            taxonomy.term_taxonomy_id = item.id + 5000
            taxonomy.term_id = item.id + 5000
            taxonomy.taxonomy = 'category'
            taxonomy.save(using='destination')
        except:
            pass

    print(
        '       --- Migrate              ---'
    )


def migrate_relation(
        section_id_list: int
):

    print(
        '          -----------------\n'
        '          -----------------\n'
        '          --- Articles - Term Relation  ---\n'
        '          -----------------\n'
        '          -----------------\n'

    )

    print(
        '       --- Generate Dictionary  ---'
    )

    list_objects = articleSelector.get_all_items_by_section_id_list(
        section_id_list=section_id_list
    )

    for item in list_objects:

        try:
            item_wp = articleSelector.get_item_by_id(id=item.id + 5000)

            taxonomy = get_taxonomy_by_id(
                term_id=item.section_id + 5000
            ).first()
            term_taxonomy = TermTaxonomy()
            term_taxonomy.object_id = item.id + 5000
            term_taxonomy.term_taxonomy_id = taxonomy.term_taxonomy_id
            term_taxonomy.save(using='destination')
            item_wp.guid.replace("category_mark", "apples")
        except:
            pass

    print(
        '       --- Migrate              ---'
    )

