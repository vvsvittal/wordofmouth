from urllib import request

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
from django.contrib import auth
from django_quill.fields import QuillField
from taggit.managers import TaggableManager
import os

# Create your models here.


# class User(AbstractUser):
#     pass


class Recipe(models.Model):
    # fields
    def rename_file(self, filename):
        upload_to = 'media/'
        ext = filename.split('.')[-1]
        if self.pk:
            filename = '{}.{}'.format(self.pk, ext)
        return os.path.join(upload_to, filename)
    def get_pk(self):
        return self.pk
    
    recipe_title = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    instructions = QuillField()
    picture = models.FileField(rename_file,null = True, blank= True)
    author = models.CharField(max_length=191)
    description = models.TextField(max_length=300, null = True, blank= True)
    tags = TaggableManager()

    
    

    # __str__() method to easily see the title
    def __str__(self):
        return self.recipe_title

    # def __str__(self):
    #     return self.description