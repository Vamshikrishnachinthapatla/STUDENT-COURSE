from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length = 100)
    descritpion = models.TextField()
    is_active = models.BooleanField(default= True)
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.title
    
class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student','course')
    
    def __str__(self):
        return f"{self.student.username} - {self.course.title}"
    
    