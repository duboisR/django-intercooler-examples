from django.urls import path

from bulk_update_ui.views import (
	BulkUpdateUIUserListView, BulkUpdateUIActivateUserListView,
	BulkUpdateUIDeactivateUserListView
)

urlpatterns = [
	path('users/', BulkUpdateUIUserListView.as_view(), name='buui_user_list'),
	path('users/activate/', BulkUpdateUIActivateUserListView.as_view(), name='buui_activate_user_list'),
	path('users/deactivate/', BulkUpdateUIDeactivateUserListView.as_view(), name='buui_deactivate_user_list'),
]
