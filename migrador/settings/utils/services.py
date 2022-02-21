from core.selectors import clean_default_db
from apps.articles.models import ArticleWp
from apps.section.models import TermWp
from apps.taxonomy.models import Taxonomy
from apps.taxonomy.models import TermTaxonomy


def render_names_definition(definition):
    new_list = []
    for row in definition:
        new_list.append(
            {'field': [get_name_attr(row['field'][0]), get_name_attr(row['field'][1])]}
        )
    return new_list


def add_functions(definition_list, translatorClass):
    for definition in definition_list:
        name_field = definition['field'][0]
        try:
            function = getattr(translatorClass, f'attribute_{name_field}')
        except:
            function = translatorClass.none_effect
        definition['function'] = function
    return definition_list


def generate_cross_definition(cross_definition_dict, translatorClass):
    new_list = render_names_definition(definition=cross_definition_dict)
    new_list = add_functions(
        definition_list=new_list,
        translatorClass=translatorClass
    )
    return new_list


def get_name_attr(attr):
    return attr.__dict__['field'].name


def get_cross_definition(cross_definition_dict, translatorClass):
    return generate_cross_definition(cross_definition_dict, translatorClass)


def clear_model_destination(model):
    queryset = model.objects.using('destination').all()
    for x in queryset:
        x.delete()


def clean_destination_and_default_tables():
    return True
    clean_default_db()
    clear_model_destination(
        model=ArticleWp
    )
    clear_model_destination(
        model=TermWp
    )
    clear_model_destination(
        model=Taxonomy
    )



