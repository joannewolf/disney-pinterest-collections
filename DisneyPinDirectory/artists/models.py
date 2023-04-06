from django.db import models

from tags.models import Tag


class Board(models.Model):
    name = models.CharField(max_length=64, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    serial_number = models.PositiveIntegerField(null=False)
    pinterest_url = models.URLField(max_length=128, null=False, blank=False)
    boards = models.ManyToManyField(Board, blank=True)

    links = models.TextField()

    def __str__(self):
        if self.name:
            return f'{self.serial_number} {self.name}'
        else:
            return f'{self.serial_number}'
