from django.http.response import HttpResponseBase
from django.shortcuts import render, HttpResponse

from django.contrib.auth.decorators import login_required


from .models import Question

# Create your views here.

@login_required(login_url="/account/login/")
def qna(request):
    question_objects = Question.objects.all()
    context_dict = {"name":"Anurag", 'questions':question_objects} 

    return render(request, "qna.html", context_dict,)

def question(request,pk):
    try:
        question_object = Question.objects.get(id=pk)
        context_dict = {"question":question_object}

    except:
        return HttpResponse("Not Found")
    return render(request, 'question.html', context_dict)

def some_question(request):
    return render(request,"some_question.html",)