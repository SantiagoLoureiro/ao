# Generated by Django 3.2.7 on 2021-10-02 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealtionIdSourceDestination',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('operation', models.TextField(default='operation', null=True)),
                ('source_id', models.IntegerField(default=1, null=True)),
                ('destination_id', models.IntegerField(default=1, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ArticleWp',
        ),
    ]
