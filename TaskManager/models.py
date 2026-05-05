from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def _str_(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=150)
    dic = models.TextField(blank=True)
    due_date = models.DateField(blank=True)
    status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Completed', 'Complete')])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    def _str_(self):
        return self.title
