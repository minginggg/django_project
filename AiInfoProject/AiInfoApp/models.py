from django.db import models

# Create your models here.
class AiShcool(models.Model):
    class_num = models.IntegerField()
    lecturer = models.CharField(max_length=30)
    class_room = models.CharField(max_length=10)
    student_num = models.IntegerField()

class AiStudent(models.Model):
    name = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=50)
    introtext =  models.models.TextField()