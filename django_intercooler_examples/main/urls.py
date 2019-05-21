from django.urls import path

from main.views import (
	ExamplesTemplateView, ClickToEditTemplateView, InfiniteScrollTemplateView,
	ClickToLoadTemplateView, BulkUpdateUITemplateView,
)

urlpatterns = [
	path('', ExamplesTemplateView.as_view(), name='examples'),
	path('click_to_edit/', ClickToEditTemplateView.as_view(), name='example_cte'),
	path('infinite_scroll/', InfiniteScrollTemplateView.as_view(), name='example_is'),
	path('click_to_load/', ClickToLoadTemplateView.as_view(), name='example_ctl'),
	path('bulk_update_ui/', BulkUpdateUITemplateView.as_view(), name='example_buui'),
]
