from django.views.generic.base import TemplateView

from artists.models import Artist, Board
from tags.models import Category, Tag


class ArtistsView(TemplateView):
    http_method_names = ['get']
    template_name = 'artists.html'

    def get_context_data(self, **kwargs):
        context = super(ArtistsView, self).get_context_data(**kwargs)
        artists = Artist.objects.all().order_by('serial_number')
        context['artists'] = [a.as_dict() for a in artists]
        return context


class ArtistDetailView(TemplateView):
    http_method_names = ['get']
    template_name = 'artist_details.html'

    def get_context_data(self, **kwargs):
        context = super(ArtistDetailView, self).get_context_data(**kwargs)

        serial_number = self.kwargs.get('artist_number')
        try:
            artist = Artist.objects.get(serial_number=serial_number)
        except Artist.DoesNotExist:
            context['error_message'] = 'Invalid artist id.'
            return context
        context['artist'] = artist.as_dict()
        print(artist.as_dict())

        category_objs = Category.objects.all().prefetch_related('tag_set')
        categories = []
        for c in category_objs:
            category_info = c.as_dict()
            category_info['tags'] = [t.as_simple_dict() for t in c.tag_set.all()]
            categories.append(category_info)
        context['categories'] = categories

        return context


class TagsView(TemplateView):
    http_method_names = ['get']
    template_name = 'tags.html'

    def get_context_data(self, **kwargs):
        context = super(TagsView, self).get_context_data(**kwargs)
        category_objs = Category.objects.all().prefetch_related('tag_set')
        categories = []
        for c in category_objs:
            category_info = c.as_dict()
            category_info['tags'] = [t.as_simple_dict() for t in c.tag_set.all()]
            categories.append(category_info)
        context['categories'] = categories
        return context


class TagDetailView(TemplateView):
    http_method_names = ['get']
    template_name = 'tag_details.html'

    def get_context_data(self, **kwargs):
        context = super(TagDetailView, self).get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            context['error_message'] = 'Invalid tag id.'
            return context
        context['tag'] = tag.as_dict()

        boards = tag.board_set.all().order_by('name')
        boards = [b.as_dict() for b in boards]
        context['boards'] = boards
        return context
