from django.views.generic import ListView, View
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse


class BulkUpdateUIUserListView(ListView):
    model = get_user_model()
    paginate_by = 5

    def get_template_names(self):
        ids = self.request.GET.getlist('ids', [])
        if ids:
            return ['bulk_update_ui/frags/user_list.html']
        return ['bulk_update_ui/base.html']

    def get_context_data(self, **kwargs):
        context = super(BulkUpdateUIUserListView, self).get_context_data(**kwargs)
        context['ids'] = self.request.GET.getlist('ids', [])
        return context


class BulkUpdateUIActivateUserListView(View):
    def post(self, request, *args, **kwargs):
        ids = self.request.POST.getlist('ids', [])
        get_user_model().objects.filter(pk__in=ids).update(is_active=True)
        return HttpResponseRedirect("%s?ids=%s" % (reverse('buui_user_list'), '&ids='.join(ids)))


class BulkUpdateUIDeactivateUserListView(View):
    def post(self, request, *args, **kwargs):
        ids = self.request.POST.getlist('ids', [])
        get_user_model().objects.filter(pk__in=ids).update(is_active=False)
        return HttpResponseRedirect("%s?ids=%s" % (reverse('buui_user_list'), '&ids='.join(ids)))
