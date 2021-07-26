

from django.urls import path
from qna import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.qna),
    path("<int:pk>",views.question),
    path("some-question/", views.some_question),
    path("about/", TemplateView.as_view(template_name="about.html") )
]