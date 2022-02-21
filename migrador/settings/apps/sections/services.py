# Sections
from apps.sections.cross_definition import cross_definition_dict as cross_definition_dict_sections
from apps.sections.translations import Translator as TranslatorSectionsClass
from apps.sections import models as SectionsModels
from apps.sections import selectors as SectionsSelector

# Core
from core.core import MigrantCore
from core.constants import Operation

# Utils
from utils.services import get_cross_definition


def migrate(
        supplement_id: int
):
    print(
        '          -----------------\n'
        '          -----------------\n'
        '          --- Sections  ---\n'
        '          -----------------\n'
        '          -----------------\n'

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
    migrator = MigrantCore(
        list_cross=definition_list_articles,
        destination_model=SectionsModels.ArticleWp,
        list_objects=SectionsSelector.get_all_items_by_supplement_id(supplement_id=supplement_id),
        operation=Operation.SECTIONS.value
    )
    migrator.migrate()

