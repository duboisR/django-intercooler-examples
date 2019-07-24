from django.views.generic import TemplateView


class HistorySupportTabTemplateView(TemplateView):
    template_name = "history_support/base.html"


class HistorySupportTab1TemplateView(TemplateView):
    template_name = "history_support/frags/tab_1.html"


class HistorySupportTab2TemplateView(TemplateView):
    template_name = "history_support/frags/tab_2.html"


class HistorySupportTab3TemplateView(TemplateView):
    template_name = "history_support/frags/tab_3.html"
