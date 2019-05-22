from django.urls import path

from lazily_loading_an_elt.views import (
	LazilyLoadingTemplateView, LazilyLoadingGraphImgTemplateView
)

urlpatterns = [
	path('graph/', LazilyLoadingTemplateView.as_view(), name='llae_graph'),
	path('graph/img/', LazilyLoadingGraphImgTemplateView.as_view(), name='llae_graph_img'),
]
