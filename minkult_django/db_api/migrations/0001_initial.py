# Generated by Django 4.2.5 on 2023-09-16 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Composer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('genre_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TextAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('creation_year', models.CharField(max_length=255, null=True)),
                ('keywords', models.TextField(default='')),
                ('composer', models.ManyToManyField(related_name='song_composer', to='db_api.composer')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='db_api.genre')),
                ('text_author', models.ManyToManyField(related_name='song_text_author', to='db_api.textauthor')),
                ('theme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='db_api.theme')),
            ],
        ),
    ]
