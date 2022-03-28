from urllib import request
from django.db import models
from django.contrib import auth
from django_quill.fields import QuillField

# Create your models here.

class Recipe(models.Model):
    # fields
    recipe_title = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    instructions = QuillField()

    # __str__() method to easily see the title
    def __str__(self):
        return self.recipe_title
