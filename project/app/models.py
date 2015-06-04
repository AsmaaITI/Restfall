from django.db import models

# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length=250)

class Book(models.Model):
	title = models.CharField(max_length=230)
	author = models.ForeignKey(Author)
	description=models.TextField()

