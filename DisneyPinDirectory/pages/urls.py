from django.urls import re_path

from pages.views import (
    GetBySerialNumberView, GetByTagView,
    GetArtistDetailView, GetTagDetailView
)


page_url_patterns = [
    re_path(r'^$', GetBySerialNumberView.as_view()),
    re_path(r'^artists/(?P<artist_number>[\d]+)$', GetArtistDetailView.as_view()),
    re_path(r'^tags$', GetByTagView.as_view()),
    re_path(r'^tags/(?P<tag_id>[\d]+)$', GetTagDetailView.as_view()),
]
