from django.urls import path

from click_to_edit.views import ClickToEditUserDetailView, ClickToEditUserUpdateView

urlpatterns = [
	path('users/<int:pk>/detail/', ClickToEditUserDetailView.as_view(), name='cte_user_detail'),
	path('users/<int:pk>/update/', ClickToEditUserUpdateView.as_view(), name='cte_user_update'),
]
