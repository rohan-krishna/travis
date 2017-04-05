from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Notebook(models.Model):
	"""docstring for Notebook"""
	title = models.CharField( max_length = 200, default = "Untitled Notebook" )
	owner = models.ForeignKey( 'auth.User' )
	created_at = models.DateTimeField( 'date created', default=timezone.now )
	updated_at = models.DateTimeField( 'date updated', default=timezone.now )

	def __str__(self):
		return self.title

class Note(models.Model):

	title = models.CharField( max_length = 200, default = "Untitled Note" )
	notebook = models.ForeignKey( Notebook, on_delete = models.CASCADE )
	body = models.TextField( blank=True, null=True )

	def __str__(self):
		return self.title
		