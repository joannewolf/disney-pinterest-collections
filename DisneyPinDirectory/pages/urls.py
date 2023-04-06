from django.urls import re_path

from pages.views import GetBySerialNumberView, GetByTagView


page_url_patterns = [
    re_path(r'^$', GetBySerialNumberView.as_view()),
    re_path(r'^serial_numbers$', GetBySerialNumberView.as_view()),
    re_path(r'^tags$', GetByTagView.as_view()),
]
