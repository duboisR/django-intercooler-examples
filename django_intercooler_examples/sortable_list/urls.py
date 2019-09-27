from django.urls import path

from sortable_list.views import SortableColorListView

urlpatterns = [
	path('colors/', SortableColorListView.as_view(), name='sl_color_list'),
]
