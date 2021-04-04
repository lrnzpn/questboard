from django.db import models

# Create your models here.
class Questboard(models.Model):
    name = models.CharField(max_length=140, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    required_stars = models.IntegerField(max_length=40, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Quest(models.Model):
    name = models.CharField(max_length=140, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    stars = models.IntegerField(max_length=7, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Slot(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    student = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.student