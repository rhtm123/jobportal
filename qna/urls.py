

from django.urls import path
from qna import views

urlpatterns = [
    path("", views.qna),
    path("some-question", views.some_question),
]