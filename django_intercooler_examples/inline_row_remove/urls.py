from django.urls import path

from inline_row_remove.views import (
	InlineRowRemoveUserListView, InlineRowRemoveUserDeleteView
)

urlpatterns = [
	path('users/', InlineRowRemoveUserListView.as_view(), name='irr_user_list'),
	path('users/<int:pk>/delete', InlineRowRemoveUserDeleteView.as_view(), name='irr_user_delete'),
]
