from django.urls import path

from job_runner.views import (
    JobRunnerTaskTemplateView, JobRunnerTaskStatusTemplateView,
    job_runner_task_run_view, job_runner_task_percent_view,
)

urlpatterns = [
    path('task/', JobRunnerTaskTemplateView.as_view(), name='jr_task'),
    path('task/status/', JobRunnerTaskStatusTemplateView.as_view(), name='jr_task_status'),
    path('task/run/', job_runner_task_run_view, name='jr_task_run'),
    path('task/percent/', job_runner_task_percent_view, name='js_task_percent'),
]
