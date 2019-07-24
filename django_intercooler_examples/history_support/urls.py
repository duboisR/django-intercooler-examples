from django.urls import path

from history_support.views import (
    HistorySupportTabTemplateView, HistorySupportTab1TemplateView,
    HistorySupportTab2TemplateView, HistorySupportTab3TemplateView
)

urlpatterns = [
    path('tab/', HistorySupportTabTemplateView.as_view(), name='hs_tab'),
    path('tab/1/', HistorySupportTab1TemplateView.as_view(), name='hs_tab_1'),
    path('tab/2/', HistorySupportTab2TemplateView.as_view(), name='hs_tab_2'),
    path('tab/3/', HistorySupportTab3TemplateView.as_view(), name='hs_tab_3'),
]
