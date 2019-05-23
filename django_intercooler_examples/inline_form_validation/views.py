from django.views.generic import CreateView, FormView
from django.contrib.auth import get_user_model

import inline_form_validation.forms


class InlineFormValidationUserCreateView(CreateView):
    template_name = 'inline_form_validation/base.html'
    model = get_user_model()
    fields = ('email', 'first_name', 'last_name')


class InlineFormValidationEmailFormView(FormView):
    template_name = 'inline_form_validation/frags/email_input.html'
    form_class = inline_form_validation.forms.EmailForm

    def form_valid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
