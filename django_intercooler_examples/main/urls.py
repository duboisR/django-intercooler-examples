from django.urls import path

from main.views import (
    ExamplesTemplateView, ClickToEditTemplateView, InfiniteScrollTemplateView,
    ClickToLoadTemplateView, BulkUpdateUITemplateView,
    LazilyLoadingAnElementView, InlineFormValidationView, InlineRowRemovalView,
    ActiveSearchView, DependentSelectView, HistorySupportView, JobRunnerView,
    SortableListView,
)

urlpatterns = [
    path('', ExamplesTemplateView.as_view(), name='examples'),
    path('click_to_edit/', ClickToEditTemplateView.as_view(), name='example_cte'),
    path('infinite_scroll/', InfiniteScrollTemplateView.as_view(), name='example_is'),
    path('click_to_load/', ClickToLoadTemplateView.as_view(), name='example_ctl'),
    path('bulk_update_ui/', BulkUpdateUITemplateView.as_view(), name='example_buui'),
    path('lazily_loading_an_elt/', LazilyLoadingAnElementView.as_view(), name='example_llae'),
    path('inline_form_validation/', InlineFormValidationView.as_view(), name='example_ifv'),
    path('inline_row_removal/', InlineRowRemovalView.as_view(), name='example_irr'),
    path('active_search/', ActiveSearchView.as_view(), name='example_as'),
    path('dependent_select/', DependentSelectView.as_view(), name='example_ds'),
    path('history_support/', HistorySupportView.as_view(), name='example_hs'),
    path('job_runner/', JobRunnerView.as_view(), name='example_jr'),
    path('sortable_list/', SortableListView.as_view(), name='example_sl'),
]
