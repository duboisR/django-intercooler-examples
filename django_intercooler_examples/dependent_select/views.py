from django.views.generic import FormView

import dependent_select.forms


class DependentSelectFormView(FormView):
    template_name = 'dependent_select/base.html'
    form_class = dependent_select.forms.GroupUserForm


class DependentSelectUserSelectFromView(FormView):
    template_name = 'dependent_select/frags/user_select.html'
    form_class = dependent_select.forms.UserForm

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
