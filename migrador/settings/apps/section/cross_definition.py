from apps.section.models import Section, TermWp

cross_definition_dict = [
    {'field': [Section.id, TermWp.term_id]},
    {'field': [Section.name, TermWp.name]},
]


