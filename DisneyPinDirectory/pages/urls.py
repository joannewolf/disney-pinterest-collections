from django.urls import re_path

from pages.views import (
    ArtistsView, ArtistDetailView,
    TagsView, TagDetailView,
)


page_url_patterns = [
    re_path(r'^$', ArtistsView.as_view()),
    re_path(r'^artists/(?P<artist_number>[\d]+)$', ArtistDetailView.as_view()),
    re_path(r'^tags$', TagsView.as_view()),
    re_path(r'^tags/(?P<tag_id>[\d]+)$', TagDetailView.as_view()),
]
