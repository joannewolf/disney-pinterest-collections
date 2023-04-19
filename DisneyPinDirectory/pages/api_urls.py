from django.urls import re_path

from pages.api_views import (
    GetArtistView, CreateArtistView, UpdateArtistView,
    GetBoardView, CreateBoardView, UpdateBoardView,
)


page_api_url_patterns = [
    re_path(r'^artists$', GetArtistView.as_view()),
    re_path(r'^artists/create$', CreateArtistView.as_view()),
    re_path(r'^artists/(?P<artist_number>[\d]+)/update$', UpdateArtistView.as_view()),
    re_path(r'^artists/(?P<artist_number>[\d]+)/boards$', GetBoardView.as_view()),
    re_path(r'^artists/(?P<artist_number>[\d]+)/board/create$', CreateBoardView.as_view()),
    re_path(r'^artists/(?P<artist_number>[\d]+)/board/(?P<board_id>[\d]+)/update$', UpdateBoardView.as_view()),
]
