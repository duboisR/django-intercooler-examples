from django.urls import path

from infinite_scroll.views import InfiniteScrollUserListView

urlpatterns = [
	path('users/', InfiniteScrollUserListView.as_view(), name='is_user_list'),
]
