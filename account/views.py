from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
# Create your views here.

def mylogout(request):
	logout(request)
	return HttpResponse('logout Successful')


def mylogin(request):
    context_dict = {'loggedIn': False}
    next = request.GET.get("next", None)
    if request.method == "POST":
        u = request.POST.get("username",None)
        p = request.POST.get("password", None)

        user = authenticate(username=u,password=p)
        if user is not None:
            login(request, user)
            context_dict['loggedIn'] = True
            if next:
                return redirect(next)


            return render(request,"login.html",context_dict)
        else:
            return HttpResponse("Username and Password not correct")


    return render(request, "login.html", context_dict)


def register(request):
    context_dict = {'created': False}
    if request.method == "POST":
        u = request.POST.get("username",None)
        p = request.POST.get("password", None)
        user = User.objects.create_user(username=u, password=p)
        user.save()

        context_dict['created'] = True

        return render(request,"register.html",context_dict)
        

    return render(request,"register.html",context_dict)
