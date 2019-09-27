from django.views.generic import ListView

from sortable_list.models import FavoriteColor


class SortableColorListView(ListView):
    model = FavoriteColor
    paginate_by = 10

    def get_template_names(self):
        if self.request.POST:
            return ['sortable_list/frags/color_list.html']
        return ['sortable_list/base.html']

    def post(self, request, *args, **kwargs):
        color_list = request.POST.getlist('colors', [])
        for i, color_pk in enumerate(color_list):
            color_instance = FavoriteColor.objects.get(pk=color_pk)
            color_instance.position = i
            color_instance.save()
        return self.get(request, *args, **kwargs)
