from django.db import models

from tags.models import Tag


class Artist(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    serial_number = models.PositiveIntegerField(null=False)
    pinterest_page_url = models.URLField(max_length=128, null=True, blank=True)

    artstation_url = models.CharField(max_length=128, null=True, blank=True)
    behance_url = models.CharField(max_length=128, null=True, blank=True)
    deviantart_url = models.CharField(max_length=128, null=True, blank=True)
    facebook_url = models.CharField(max_length=128, null=True, blank=True)
    instagram_url = models.CharField(max_length=128, null=True, blank=True)
    pinterest_url = models.CharField(max_length=128, null=True, blank=True)
    pixiv_url = models.CharField(max_length=128, null=True, blank=True)
    tumblr_url = models.CharField(max_length=128, null=True, blank=True)
    twitter_url = models.CharField(max_length=128, null=True, blank=True)
    weibo_url = models.CharField(max_length=128, null=True, blank=True)
    other_url = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        if self.name:
            return f'{self.serial_number:03} {self.name}'
        else:
            return f'{self.serial_number:03}'


class Board(models.Model):
    name = models.CharField(max_length=64, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
