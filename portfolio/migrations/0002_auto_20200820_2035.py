# Generated by Django 3.0.8 on 2020-08-20 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acadexp',
            old_name='position',
            new_name='qualification',
        ),
    ]
