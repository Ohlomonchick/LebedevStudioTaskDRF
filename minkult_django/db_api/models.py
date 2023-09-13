from django.db import models


class Composer(models.Model):
    name = models.CharField(max_length=255)


class TextAuthor(models.Model):
    name = models.CharField(max_length=255)


class Genre(models.Model):
    name = models.CharField(max_length=255)
    genre_id = models.fields.CharField()


class Theme(models.Model):
    name = models.CharField(max_length=255)


class Song(models.Model):
    name = models.fields.TextField()
    composer = models.ManyToManyField(
        Composer,
        related_name="song_composer",
    )
    creation_year = models.fields.CharField(null=True)
    text_author = models.ManyToManyField(
        TextAuthor,
        related_name="song_text_author",
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        null=True
    )
    theme = models.ForeignKey(
        Theme,
        on_delete=models.CASCADE,
        null=True
    )
    keywords = models.fields.TextField(default="")




    



