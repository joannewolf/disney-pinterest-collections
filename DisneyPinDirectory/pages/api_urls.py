from django.urls import re_path

from pages.api_views import (
    GetBoardView, CreateBoardView, UpdateBoardView,
)


page_api_url_patterns = [
    re_path(r'^artists/(?P<artist_number>[\d]+)/boards$', GetBoardView.as_view()),
    re_path(r'^artists/(?P<artist_number>[\d]+)/board/create$', CreateBoardView.as_view()),
    re_path(r'^artists/(?P<artist_number>[\d]+)/board/(?P<board_id>[\d]+)/update$', UpdateBoardView.as_view()),
]
