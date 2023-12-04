# Generated by Django 4.0.2 on 2023-12-04 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_alter_ticket_movie_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='actors', to='db.Actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='genres', to='db.Genre'),
        ),
        migrations.AlterField(
            model_name='moviesession',
            name='cinema_hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cinema_halls', to='db.cinemahall'),
        ),
        migrations.AlterField(
            model_name='moviesession',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='db.movie'),
        ),
    ]
