# Local Imports
# Core
from core.core import MigrantCore
from core.constants import Operation

# Utils
from utils.services import get_cross_definition

# Articles
from apps.articles import models as ArticlesModels
from apps.articles import selectors as articlesSelector
from apps.articles.cross_definition import cross_definition_dict as cross_definition_dict_articles
from apps.articles.translator import Translator as TranslatorArticleClass


def migrate(section_id_list):

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
    list_objects = articlesSelector.get_all_items_by_section_id_list(
        section_id_list=section_id_list
    )

    definition_list_articles = get_cross_definition(
        cross_definition_dict=cross_definition_dict_articles,
        translatorClass=TranslatorArticleClass
    )
    print(
        '       --- Migrate              ---'
    )
    migrator = MigrantCore(
        list_cross=definition_list_articles,
        destination_model=ArticlesModels.ArticleWp,
        list_objects=list_objects,
        operation=Operation.ARTICLES.value
    )
    migrator.migrate()
