# Sections
from apps.section.cross_definition import cross_definition_dict as cross_definition_dict_sections
from apps.section.translations import Translator as TranslatorSectionsClass
from apps.section import models as SectionsModels
from apps.section import selectors as SectionsSelector

# Core
from core.core import MigrantCore
from core.constants import Operation

# Utils
from utils.services import get_cross_definition


def migrate(
        supplement_id: int
):
    print(
        '          ------------------\n'
        '          ------------------\n'
        '          -Sections To Term-\n'
        '          ------------------\n'
        '          ------------------\n'

    )

    print(
        '       --- Generate Dictionary  ---'
    )

    definition_list_articles = get_cross_definition(
        cross_definition_dict=cross_definition_dict_sections,
        translatorClass=TranslatorSectionsClass
    )
    print(
        '       --- Migrate              ---\n\n\n'
    )

    print(SectionsSelector.get_all_items_by_supplement_id(supplement_id=supplement_id)[1].__dict__)
    migrator = MigrantCore(
        list_cross=definition_list_articles,
        destination_model=SectionsModels.TermWp,
        list_objects=SectionsSelector.get_all_items_by_supplement_id(supplement_id=supplement_id),
        operation=Operation.SECTIONS.value
    )
    migrator.migrate()

