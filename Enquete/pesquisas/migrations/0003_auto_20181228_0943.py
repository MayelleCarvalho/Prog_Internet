# Generated by Django 2.0 on 2018-12-28 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pesquisas', '0002_auto_20181228_0915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opcoes',
            old_name='quastao',
            new_name='questao',
        ),
    ]
