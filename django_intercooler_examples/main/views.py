from django.views.generic import TemplateView
from django.contrib.auth import get_user_model


class ExamplesTemplateView(TemplateView):
    template_name = "main/examples.html"


class ClickToEditTemplateView(TemplateView):
    template_name = "main/example_cte.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Select a random user
        context['user'] = get_user_model().objects.order_by("?").first()
        return context


class InfiniteScrollTemplateView(TemplateView):
    template_name = "main/example_is.html"


class ClickToLoadTemplateView(TemplateView):
    template_name = "main/example_ctl.html"


class BulkUpdateUITemplateView(TemplateView):
    template_name = "main/example_buui.html"


class LazilyLoadingAnElementView(TemplateView):
    template_name = "main/example_llae.html"


class InlineFormValidationView(TemplateView):
    template_name = "main/example_ifv.html"


class InlineRowRemovalView(TemplateView):
    template_name = "main/example_irr.html"


class ActiveSearchView(TemplateView):
    template_name = "main/example_as.html"


class DependentSelectView(TemplateView):
    template_name = "main/example_ds.html"


class HistorySupportView(TemplateView):
    template_name = "main/example_hs.html"


class JobRunnerView(TemplateView):
    template_name = "main/example_jr.html"


class SortableListView(TemplateView):
    template_name = "main/example_sl.html"
