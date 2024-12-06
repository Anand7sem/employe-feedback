from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    is_anonymous = models.BooleanField(default=False)

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survey_id = models.IntegerField()
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)