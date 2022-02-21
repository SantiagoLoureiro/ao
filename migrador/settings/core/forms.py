from django import forms
from apps.supplements.constants import SUPPLEMENT_LIST


class DatabaseInfoForm(forms.Form):
    name = forms.CharField(label='Database Name',
                                   max_length=100,
                                   widget=forms.TextInput(
                                       attrs=
                                          {
                                              'placeholder': 'database name',
                                              'class': "field",
                                              'value': "wordpress"
                                          }
                                    )
                                   )
    host = forms.CharField(label='Database Host',
                                   max_length=100,
                                   widget=forms.TextInput(
                                       attrs=
                                          {
                                              'placeholder': 'database host',
                                              'class': "field",
                                              'value': 'localhost'
                                          }
                                    )
                                   )
    port = forms.CharField(label='Database Port',
                                   max_length=100,
                                   widget=forms.TextInput(
                                       attrs=
                                          {
                                              'placeholder': 'database port',
                                              'class': "field",
                                              'value': '3306'
                                          }
                                    )
                                   )
    user = forms.CharField(label='Database User',
                                   max_length=100,
                                   widget=forms.TextInput(
                                       attrs=
                                          {
                                              'placeholder': 'database user',
                                              'class': "field",
                                              'value': "test"
                                          }
                                    )
                                   )
    password = forms.CharField(label='Database Password',
                                   max_length=100,
                                   widget=forms.TextInput(
                                       attrs=
                                          {
                                              'placeholder': 'database password',
                                              'class': "field",
                                              'value': "test"
                                          }
                                    )
                                   )
    clean_database = forms.BooleanField(
                                      required=False,
                                      initial=True,
                                      label='Clean Database')

    page = forms.CharField(
        max_length=30,
        widget=forms.Select(choices=SUPPLEMENT_LIST),
    )