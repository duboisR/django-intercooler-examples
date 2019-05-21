from django.views.generic import DetailView, UpdateView
from django.contrib.auth import get_user_model
from django.urls import reverse


class ClickToEditUserDetailView(DetailView):
    model = get_user_model()

    def get_template_names(self):
        block = self.request.GET.get('block', None)
        if block == '':
            return ['click_to_edit/frags/user_detail.html']
        return ['click_to_edit/base.html']


class ClickToEditUserUpdateView(UpdateView):
    template_name = "click_to_edit/frags/user_form.html"
    model = get_user_model()
    fields = ('email', 'first_name', 'last_name')

    def get_success_url(self):
        view_name = 'cte_user_detail'
        return "%s?block" % reverse(view_name, kwargs={'pk': self.object.pk})
