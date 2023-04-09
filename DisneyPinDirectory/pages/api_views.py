import http.client as httplib

from django.db import transaction
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView, View

from artists.models import Artist, Board
from DisneyPinDirectory.mixins import CsrfExemptMixin
from DisneyPinDirectory.utils import error_json_response, form_error_json_response
from pages.forms import CreateAndUpdateBoardForm
from tags.models import Tag


class CreateBoardView(CsrfExemptMixin, FormView):
    http_method_names = ['post']
    form_class = CreateAndUpdateBoardForm

    @transaction.atomic
    def form_valid(self, form):
        artist_number = self.kwargs.get('artist_number')
        try:
            artist = Artist.objects.get(serial_number=artist_number)
        except Artist.DoesNotExist:
            return error_json_response(
                code='invalid',
                message='Invalid artist id.',
            )

        name = form.cleaned_data['name']
        tag_ids = form.cleaned_data['tag_ids'].split(',')

        tags = []
        for tag_id in tag_ids:
            try:
                tag = Tag.objects.get(id=tag_id)
            except Tag.DoesNotExist:
                return error_json_response(
                code='invalid',
                message=f'Invalid tag id {tag_id}.',
            )
            tags.append(tag)

        board = Board.objects.create(
            artist=artist,
            name=f'{artist.serial_number:03}.{name}',
        )
        for tag in tags:
            board.tags.add(tag)

        response = {
            'data': board.as_dict(),
        }
        return JsonResponse(response, status=httplib.OK)

    def form_invalid(self, form):
        return form_error_json_response(form.errors)


class UpdateBoardView(CsrfExemptMixin, FormView):
    http_method_names = ['post']
    form_class = CreateAndUpdateBoardForm

    @transaction.atomic
    def form_valid(self, form):
        author_id = self.kwargs.get('author_id')
        try:
            author = Author.objects.get(id=author_id)
        except Author.DoesNotExist:
            return error_json_response(
                code='invalid',
                message=_('Invalid author id.'),
            )

        before_data = author.as_json_str()

        name = form.cleaned_data['name']
        author.name = name
        author.save()


        response = {
            'data': author.as_dict(),
        }
        return JsonResponse(response, status=httplib.OK)

    def form_invalid(self, form):
        return form_error_json_response(form.errors, AdminPageConfig.name, 'CreateAndUpdateAuthorForm')

