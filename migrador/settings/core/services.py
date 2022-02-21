# Local Imports
from apps.articles.services import migrate as migrate_articles
from apps.sections.services import migrate as migrate_sections
from apps.section.services import migrate as migrate_sections_to_term
from apps.taxonomy.services import migrate as migrate_taxonomy
from apps.taxonomy.services import migrate_relation as migrate_taxonomy_relationship
from apps.sections.selectors import get_list_ids_by_supplement_id
from settings.settings import DATABASES


def config_database(
        name: str,
        host: str,
        user: str,
        password: str,
        port: str
):
    destination_db_config = DATABASES['destination']
    destination_db_config['NAME'] = name
    destination_db_config['USER'] = user
    destination_db_config['PASSWORD'] = password
    destination_db_config['HOST'] = host
    destination_db_config['PORT'] = port


def migrate(supplement_id):

    print(
        '          ----------------------------------------------------\n'
        '          ----------------------------------------------------\n'
        '          ---------------------Migrador-----------------------\n'
        '          ----------------------------------------------------\n'
        '          ----------------------------------------------------\n'

    )

    section_id_list = get_list_ids_by_supplement_id(
        supplement_id=supplement_id
    )

    migrate_sections(
        supplement_id=supplement_id
    )

    migrate_sections_to_term(
        supplement_id=supplement_id
    )


    migrate_taxonomy(
        supplement_id=supplement_id
    )

    migrate_articles(
       section_id_list=section_id_list
    )

    migrate_taxonomy_relationship(
        section_id_list=section_id_list
    )





