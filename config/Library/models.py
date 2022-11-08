from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.Charfield(max_length=200, on_delete=models.CASCADE)
    author = models.Charfield(max_length=200)
    genre = models.Charfield(max_length=50)
    pubdate = models.DateField()
    isFeatured = models.BooleanField()

def __str__(self):
    return self.title