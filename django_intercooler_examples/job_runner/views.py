from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView


class JrTask:
    """ Mock Background Task """

    def __init__(self):
        self.start()

    def start(self):
        self.complete = False
        self.percent = 0

    def progress(self):
        self.percent += 10
        if self.percent >= 100:
            self.complete = True
            self.percent = 100


jr_task = JrTask()


class JobRunnerTaskTemplateView(TemplateView):
    template_name = "job_runner/base.html"


class JobRunnerTaskStatusTemplateView(TemplateView):
    template_name = "job_runner/frags/status.html"

    def get_context_data(self, **kwargs):
        context = super(JobRunnerTaskStatusTemplateView, self).get_context_data(**kwargs)
        context['complete'] = jr_task.complete
        return context


@csrf_exempt
def job_runner_task_run_view(request):
    jr_task.start()
    return redirect(reverse('jr_task_status'))


@csrf_exempt
def job_runner_task_percent_view(request):
    jr_task.progress()
    percent = "{percent}%".format(percent=jr_task.percent)
    response = HttpResponse(percent)
    if jr_task.complete:
        response['X-IC-Refresh'] = reverse('jr_task_status')
    return response
