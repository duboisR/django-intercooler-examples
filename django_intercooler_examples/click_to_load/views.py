from django.views.generic import ListView
from django.contrib.auth import get_user_model


class ClickToLoadUserListView(ListView):
    model = get_user_model()
    paginate_by = 5

    def get_template_names(self):
        page = int(self.request.GET.get('page', "0"))
        if page > 1:
            return ['click_to_load/frags/user_list.html']
        return ['click_to_load/base.html']
