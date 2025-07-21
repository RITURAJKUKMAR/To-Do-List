from django.urls import path
from LOGIN_Assig.views import *

app_name = "LOGIN_Assig"

urlpatterns = [
    path("", login, name="login"),
    path("registration", registration, name="registration"),
    path("home", home, name="home"),
    path("profile", profile, name="profile"),
    path("saveData", saveData, name="saveData"),
    path("toDoListDelete", toDoListDelete, name="toDoListDelete"),
    path("workDone", workDone, name="workDone"),
    path("logout", logout, name="logout"),
]
