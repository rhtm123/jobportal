from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def qna(request):
    return HttpResponse("QNA")

def some_question(request):
    return render(request,"some_question.html",)