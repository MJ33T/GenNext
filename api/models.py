from django.db import models
from django.contrib.auth.models import User



class Task(models.Model):
    task_name = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.TextField()
    assign = models.ForeignKey(User, on_delete=models.CASCADE)
    complete_status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self
    
class Comment(models.Model):
    commenter_name = models.CharField(max_length=100)
    comment_text = models.TextField()
    tas_id = models.ForeignKey(Task, on_delete=models.CASCADE, default= 0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self


