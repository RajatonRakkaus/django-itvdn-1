# Generated by Django 3.2.7 on 2021-09-09 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_8', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamemodel',
            old_name='years',
            new_name='year',
        ),
    ]