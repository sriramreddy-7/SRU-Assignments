from django.db import models

# Create your models here.

class Assigments(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='')
    subject = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    assignment_file = models.FileField(upload_to='assignments/')  # Removed the default value
    posted_by = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.title