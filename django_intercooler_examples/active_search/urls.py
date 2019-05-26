from django.urls import path

from active_search.views import ActiveSearchUserListView

urlpatterns = [
	path('users/', ActiveSearchUserListView.as_view(), name='as_user_list'),
]
