from django.views.generic import TemplateView

import time


class LazilyLoadingTemplateView(TemplateView):
    template_name = 'lazily_loading_an_elt/base.html'


class LazilyLoadingGraphImgTemplateView(TemplateView):
    template_name = 'lazily_loading_an_elt/graph.html'

    def get_context_data(self, **kwargs):
        context = super(LazilyLoadingGraphImgTemplateView, self).get_context_data(**kwargs)
        # Wait for 5 seconds
        time.sleep(5)
        return context
