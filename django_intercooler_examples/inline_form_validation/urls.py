from django.urls import path

from inline_form_validation.views import (
	InlineFormValidationUserCreateView, InlineFormValidationEmailFormView
)

urlpatterns = [
	path('user/', InlineFormValidationUserCreateView.as_view(), name='ifv_user'),
	path('user/email/', InlineFormValidationEmailFormView.as_view(), name='ifv_user_email'),
]
