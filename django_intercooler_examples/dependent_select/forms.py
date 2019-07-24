from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


class UserForm(forms.Form):
    user = forms.ModelChoiceField(queryset=get_user_model().objects.all(), empty_label=None)

    def __init__(self, *args, **kwargs):
        group_pk = kwargs.get('data', {}).get('group', None)
        super(UserForm, self).__init__(*args, **kwargs)
        if group_pk:
            self.fields['user'].queryset = Group.objects.get(pk=group_pk).user_set.all()


class GroupUserForm(UserForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), empty_label="All")
