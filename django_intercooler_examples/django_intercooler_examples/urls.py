"""django_intercooler_examples URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('main.urls')),
    path('click_to_edit/', include('click_to_edit.urls')),
    path('infinite_scroll/', include('infinite_scroll.urls')),
    path('click_to_load/', include('click_to_load.urls')),
    path('bulk_update_ui/', include('bulk_update_ui.urls')),
    path('lazily_loading_an_elt/', include('lazily_loading_an_elt.urls')),
    path('inline_form_validation/', include('inline_form_validation.urls')),
    path('inline_row_remove/', include('inline_row_remove.urls')),
    path('active_search/', include('active_search.urls')),
]
