# Generated by Django 3.2.7 on 2021-09-09 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_8', '0002_rename_years_gamemodel_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='GamerLibraryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('game', models.ManyToManyField(to='lesson_8.GameModel')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lesson_8.gamermodel')),
            ],
        ),
    ]
