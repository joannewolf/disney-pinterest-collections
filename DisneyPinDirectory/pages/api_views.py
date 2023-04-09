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


class GetBoardView(View):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        artist_number = self.kwargs.get('artist_number')
        try:
            artist = Artist.objects.get(serial_number=artist_number)
        except Artist.DoesNotExist:
            return error_json_response(
                code='invalid',
                message='Invalid artist id.',
            )

        boards = Board.objects.filter(artist=artist).order_by('name')
        data = [b.as_simple_dict() for b in boards]

        response = {
            'data': data,
        }
        return JsonResponse(response, status=httplib.OK)


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
        print(name, tag_ids)

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
            name=name,
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
        artist_number = self.kwargs.get('artist_number')
        try:
            artist = Artist.objects.get(serial_number=artist_number)
        except Artist.DoesNotExist:
            return error_json_response(
                code='invalid',
                message='Invalid artist id.',
            )

        board_id = self.kwargs.get('board_id')
        try:
            board = Board.objects.get(id=board_id)
        except Board.DoesNotExist:
            return error_json_response(
                code='invalid',
                message='Invalid board id.',
            )
        if board.artist != artist:
            return error_json_response(
                code='invalid',
                message='The board does not belong to the artist.',
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

        board.name = name
        board.tags.clear()
        for tag in tags:
            board.tags.add(tag)
        board.save()

        response = {
            'data': board.as_dict(),
        }
        return JsonResponse(response, status=httplib.OK)

    def form_invalid(self, form):
        return form_error_json_response(form.errors)
