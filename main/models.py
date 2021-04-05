from django.db import models

import re

# Create your models here.
class Questboard(models.Model):
    name = models.CharField(max_length=140, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    required_stars = models.IntegerField(blank=True, null=True)
    slug = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def create_slug(self):
        return re.sub('[^A-Za-z0-9 ]+', '', self.name).replace(' ', '-').lower()
     
    def save(self, *args, **kwargs):
        self.slug = self.create_slug()
        super(Questboard, self).save(*args, **kwargs)

class Quest(models.Model):
    questboard = models.ForeignKey(Questboard, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=140, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    stars = models.IntegerField(blank=True, null=True)
    slug = models.CharField(max_length=140, null=True, blank=True)
    is_for_everyone = models.BooleanField(default=False)
    slots = models.IntegerField(blank=True, null=True, default=0)
    
    def __str__(self):
        return self.name
    
    def create_slug(self):
    	return re.sub('[^A-Za-z0-9 ]+', '', self.name).replace(' ', '-').lower()
 
    def save(self, *args, **kwargs):
        self.slug = self.create_slug()
        super(Quest, self).save(*args, **kwargs)
                
                
class Slot(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, null=True)
    student = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.student
    
    