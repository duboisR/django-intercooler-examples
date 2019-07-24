from django.urls import path

from dependent_select.views import (
    DependentSelectFormView, DependentSelectUserSelectFromView
)

urlpatterns = [
    path('form/', DependentSelectFormView.as_view(), name='ds_form'),
    path('form/user_select/', DependentSelectUserSelectFromView.as_view(), name='ds_form_user_select'),
]
