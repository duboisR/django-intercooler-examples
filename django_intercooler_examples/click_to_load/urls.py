from django.urls import path

from click_to_load.views import ClickToLoadUserListView

urlpatterns = [
	path('users/', ClickToLoadUserListView.as_view(), name='ctl_user_list'),
]
