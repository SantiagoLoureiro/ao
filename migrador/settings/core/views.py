# Django imports
from django.shortcuts import render

# Local improts
from core import forms
from core.services import config_database, migrate
from utils.services import clean_destination_and_default_tables


def home(request):
    if request.method == 'POST':
        form = forms.DatabaseInfoForm(request.POST)
        if form.is_valid():
            config_database(
                name=form.data['name'],
                password=form.data['password'],
                host=form.data['host'],
                user=form.data['user'],
                port=form.data['port']
            )
            if 'clean_database' in form.data.keys():
                clean_destination_and_default_tables()
            migrate(
                supplement_id=form.data['page']
            )
    else:
        form = forms.DatabaseInfoForm(request.POST)

    return render(request, 'home.html', {'form': form})
