from django.db import models

# Create your models here.

class Link(models.Model):
    url = models.URLField()
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label
    
class Technology(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    links = models.ManyToManyField(Link, related_name='projects')
    technologies = models.ManyToManyField(Technology, related_name='projects')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return self.title