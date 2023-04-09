from django.db import models
from DisneyPinDirectory.utils import getUrlList

from tags.models import Tag


class Artist(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    serial_number = models.PositiveIntegerField(null=False, unique=True)
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

    def as_dict(self):
        return {
            'name': self.name,
            'serial_number': f'{self.serial_number:03}',
            'pinterest_page_url': self.pinterest_page_url,
            'artstation_url': getUrlList(self.artstation_url),
            'behance_url': getUrlList(self.behance_url),
            'deviantart_url': getUrlList(self.deviantart_url),
            'facebook_url': getUrlList(self.facebook_url),
            'instagram_url': getUrlList(self.instagram_url),
            'pinterest_url': getUrlList(self.pinterest_url),
            'pixiv_url': getUrlList(self.pixiv_url),
            'tumblr_url': getUrlList(self.tumblr_url),
            'twitter_url': getUrlList(self.twitter_url),
            'weibo_url': getUrlList(self.weibo_url),
            'other_url': getUrlList(self.other_url),
            'boards': [b.as_simple_dict() for b in self.board_set.all()]
        }


class Board(models.Model):
    name = models.CharField(max_length=64, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
            'name': self.name,
            'artist': self.artist.as_dict(),
            'tags': [t.as_dict() for t in self.tags.all()],
        }

    def as_simple_dict(self):
        return {
            'name': self.name,
            'tags': [t.as_simple_dict() for t in self.tags.all()],
        }
