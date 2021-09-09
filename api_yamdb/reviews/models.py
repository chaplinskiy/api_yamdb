from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Genres(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Titles(models.Model):
    name = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True, null=True)
    genre = models.ManyToManyField(Genres)
    category = models.ForeignKey(
        Categories, null=True, blank=True, on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name
