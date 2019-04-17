from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=256)
    
    
class Lesson(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    course = models.ForeignKey(Course,related_name='lessons',on_delete = models.CASCADE)

class Exercise(models.Model):
    title = models.CharField(max_length=256)
    problem = models.TextField()
    solution = models.TextField()
    course = models.ForeignKey(Course,related_name='exercises',on_delete = models.CASCADE) 
    lesson = models.ForeignKey(Lesson,related_name='exercises',on_delete = models.CASCADE)

class Reference(models.Model):
    title = models.CharField(max_length=256)
    link = models.TextField()
    course = models.ForeignKey(Course,related_name='reference',on_delete = models.CASCADE)
    lesson = models.ForeignKey(Lesson,related_name='reference',on_delete = models.CASCADE)
