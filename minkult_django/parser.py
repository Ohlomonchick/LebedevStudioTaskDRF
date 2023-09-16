import os
import django
import csv
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'minkult_django.settings')
django.setup()

from db_api.models import *
from django.db import transaction

composers = {}
authors = {}
genres = {}
themes = {}

songs_to_create = []
songs_to_create_m2m = []  # value = ([authors], [composers])


def proceed_many2many_cell(cell, field_class, field_dict):
    if cell:
        cell_members = [x.strip() for x in re.split(";|,", cell)]
        for member in cell_members:
            field_dict[member] = field_class(name=member)

        return cell_members
    return []


with open('data/data-1-structure-1.csv', encoding="utf-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    headers = next(spamreader)

    for row in spamreader:
        current_composers = proceed_many2many_cell(row[1], Composer, composers)
        current_authors = proceed_many2many_cell(row[3], TextAuthor, authors)

        if row[4] and row[4] not in genres.keys():
            genres[row[4]] = Genre(name=row[4], genre_id=row[5])
        if row[6] and row[6] not in themes.keys():
            themes[row[6]] = Theme(name=row[6])

        songs_to_create.append((
            row[0],
            row[2],
            row[4],
            row[6],
            row[7]
        ))
        songs_to_create_m2m.append((current_composers, current_authors))

Composer.objects.bulk_create(composers.values())
TextAuthor.objects.bulk_create(authors.values())
Genre.objects.bulk_create(genres.values())
Theme.objects.bulk_create(themes.values())

songs_to_create = [
    Song(
        name=s[0],
        creation_year=s[1] if s[1] else None,
        genre_id=genres[s[2]].pk if s[2] else None,
        theme_id=themes[s[3]].pk if s[3] else None,
        keywords=s[4]
    )
    for s in songs_to_create]

m2m_relation_composers = []
m2m_relation_authors = []
Song.objects.bulk_create(songs_to_create)

for song, song_m2m in zip(songs_to_create, songs_to_create_m2m):
    for composer in song_m2m[0]:
        m2m_relation_composers.append(Song.composer.through(song_id=song.pk, composer_id=composers[composer].pk))
    for author in song_m2m[1]:
        m2m_relation_authors.append(Song.text_author.through(song_id=song.pk, textauthor_id=authors[author].pk))

Song.composer.through.objects.bulk_create(m2m_relation_composers)
Song.text_author.through.objects.bulk_create(m2m_relation_authors)
