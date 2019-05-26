from django.views.generic import ListView, DeleteView
from django.contrib.auth import get_user_model
from django.http import HttpResponse


class InlineRowRemoveUserListView(ListView):
    template_name = 'inline_row_remove/base.html'
    model = get_user_model()
    paginate_by = 5


class InlineRowRemoveUserDeleteView(DeleteView):
    model = get_user_model()

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # self.object.delete()
        response = HttpResponse('')
        response['X-IC-Remove'] = "1s"
        return response
