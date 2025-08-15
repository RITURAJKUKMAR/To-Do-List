from django.shortcuts import render
from LOGIN_Assig.models import *
from datetime import datetime
from django.utils import timezone


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        userN = User.objects.filter(username=username)
        if len(userN) == 0:
            loginError = "Invalid email or password"
            return render(request, "login.html", {"loginError": loginError})
        # elif len(userN):
        else:
            user = User.objects.filter(username=username, password=password)
            if len(user) == 0:
                newUser = User()
                newUser.username = userN.first().username
                newUser.password = userN.first().password
                newUser.fullName = userN.first().fullName
                if userN.first().loginTimes >= 5:
                    newUser.loginTimes = 0
                else:
                    newUser.loginTimes = userN.first().loginTimes + 1
                loginTimes = newUser.loginTimes
                print("Time ...", newUser.loginTimes)
                newUser.save()
                return render(request, "login.html", {"loginTimes": str(loginTimes)})
            else:
                newUser = User()
                newUser.username = userN.first().username
                newUser.password = userN.first().password
                newUser.fullName = userN.first().fullName
                newUser.loginTimes = 0
                newUser.save()
                request.session["username"] = user.first().username
                request.session["fullName"] = user.first().fullName
                return home(request)
    else:
        if "username" not in request.session.keys():
            return render(request, "login.html")
        else:
            return home(request)


def home(request):
    if "username" not in request.session.keys():
        return render(request, "login.html")
    else:
        toDoLists = ToDoList.objects.filter(Username=request.session["username"])
        context = {
            "toDoLists": toDoLists,
        }
        return render(request, "home.html", context)


def saveData(request):
    if "username" not in request.session.keys():
        return render(request, "login.html")
    if request.method == "POST":
        userData = ToDoList()
        userData.Username = User.objects.get(username=request.session["username"])
        userData.data = request.POST["data"]
        userData.save()
    return home(request)


def toDoListDelete(request):
    if "username" not in request.session.keys():
        return render(request, "login.html")
    else:
        toDoList = 0
        try:
            toDoList = ToDoList.objects.filter(
                toDoListId=request.POST["toDoListId"]
            ).first()
        except:
            try:
                toDoList = ToDoList.objects.filter(
                    toDoListId=request.GET["toDoListId"]
                ).first()
            except:
                pass
        if toDoList:
            toDoList.delete()
    return home(request)


def workDone(request):
    if "username" not in request.session.keys():
        return render(request, "login.html")
    else:
        toDoList = 0
        try:
            toDoList = ToDoList.objects.filter(
                toDoListId=request.POST["toDoListId"]
            ).first()
        except:
            try:
                toDoList = ToDoList.objects.filter(
                    toDoListId=request.GET["toDoListId"]
                ).first()
            except:
                pass
        if toDoList:    
            doList = ToDoList()
            doList.toDoListId = toDoList.toDoListId
            doList.Username = User.objects.get(username=request.session["username"])
            doList.data = toDoList.data
            doList.status = True
            doList.data = doList.data
            doList.save()
    return home(request)


def registration(request):
    if request.method == "POST":
        username = request.POST["username"]
        if len(User.objects.filter(username=username)):
            userStatus = 1
        else:
            user = User()
            user.username = request.POST["username"]
            user.fullName = request.POST["name"]
            user.password = request.POST["password"]
            user.save()
            return render(request, "login.html")
    else:
        return render(request, "registration.html")


def profile(request):
    if "username" not in request.session.keys():
        return render(request, "login.html")
    return home(request)


def logout(request):
    if "email" in request.session.keys():
        del request.session["username"]
        del request.session["fullName"]
    return render(request, "login.html")
