from django.views.generic.base import TemplateView


class GetBySerialNumberView(TemplateView):
    http_method_names = ['get']
    template_name = 'by_serial_number.html'

    def get_context_data(self, **kwargs):
        context = super(GetBySerialNumberView, self).get_context_data(**kwargs)
        return context


class GetByTagView(TemplateView):
    http_method_names = ['get']
    template_name = 'by_tags.html'

    def get_context_data(self, **kwargs):
        context = super(GetByTagView, self).get_context_data(**kwargs)
        return context
