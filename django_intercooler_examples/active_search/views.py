from django.views.generic import ListView
from django.contrib.auth import get_user_model


class ActiveSearchUserListView(ListView):
    model = get_user_model()
    paginate_by = 10

    def get_template_names(self):
        if self.request.POST:
            return ['active_search/frags/user_list.html']
        return ['active_search/base.html']

    def get_queryset(self):
        search = self.request.POST.get('search', None)
        if search:
            return get_user_model().objects.filter(username__icontains=search)
        return get_user_model().objects.all()

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
