from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    fullName = models.CharField(null=False, max_length=30)
    password = models.CharField(null=False, max_length=20)
    loginTimes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.username)


class UserData(models.Model):
    UserDataId = models.BigAutoField(primary_key=True, auto_created=True)


class ToDoListId(models.Model):
    toDoListId = models.BigAutoField(primary_key=True, auto_created=True)
    Username = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.CharField(null=True, max_length=500)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.Username.username)


class WorkDone(models.Model):
    workDoneId = models.BigAutoField(primary_key=True, auto_created=True)
    Username = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.CharField(null=True, max_length=500)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.Username.username)
