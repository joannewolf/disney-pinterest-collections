from django.views.generic.base import TemplateView

from artists.models import Artist


class GetBySerialNumberView(TemplateView):
    http_method_names = ['get']
    template_name = 'serial_numbers.html'

    def get_context_data(self, **kwargs):
        context = super(GetBySerialNumberView, self).get_context_data(**kwargs)
        artists = Artist.objects.all().order_by('serial_number')
        context['artists'] = [a.as_dict() for a in artists]
        return context


class GetByTagView(TemplateView):
    http_method_names = ['get']
    template_name = 'tags.html'

    def get_context_data(self, **kwargs):
        context = super(GetByTagView, self).get_context_data(**kwargs)
        return context


class GetArtistDetailView(TemplateView):
    http_method_names = ['get']
    template_name = 'artist_details.html'

    def get_context_data(self, **kwargs):
        context = super(GetArtistDetailView, self).get_context_data(**kwargs)
        serial_number = self.kwargs.get('artist_number')
        try:
            artist = Artist.objects.get(serial_number=serial_number)
        except Artist.DoesNotExist:
            context['error_message'] = 'Invalid artist id.'
            return context

        context['artist'] = artist.as_dict()
        return context


class GetTagDetailView(TemplateView):
    http_method_names = ['get']
    template_name = 'tags.html'

    def get_context_data(self, **kwargs):
        context = super(GetTagDetailView, self).get_context_data(**kwargs)
        return context
