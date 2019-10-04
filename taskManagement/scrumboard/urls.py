from django.conf.urls import url
from django.views.generic import TemplateView

from .api import ListApi, CardApi

urlpatterns = [
    url('lists$', ListApi.as_view()),
    url('cards$', CardApi.as_view()),
    url('home', TemplateView.as_view(template_name="scrumboard/home.html")),
]
