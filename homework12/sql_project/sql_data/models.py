from django.db import models


class Student(models.Model):
    last_name = models.CharField("Surname", max_length=250)
    first_name = models.CharField("Name", max_length=250)
    new_value = models.CharField("Name", max_length=250)


class Teacher(models.Model):
    last_name = models.CharField("Surname", max_length=250)
    first_name = models.CharField("Name", max_length=250)
    models.CharField("Name", max_length=250)


class Homework(models.Model):
    text = models.CharField("Text", max_length=250)
    deadline = models.DateTimeField("Deadline")
    created = models.DateTimeField("When was created")
    time = models.CharField(default="timezone.now")


class HomeworkResult(models.Model):
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution = models.CharField("Solution", max_length=250)
    created = models.DateTimeField("When was created")
    time = models.CharField(default="timezone.now")
