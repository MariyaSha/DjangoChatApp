from django.db import models

# Create your models here.

class User(models.Model):
	# auto incrementing id is provided by Django by default
	name = models.CharField(max_length=25)
	password = models.CharField(max_length=25)
	authority_level = models.IntegerField(default=0)
	is_online = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Message(models.Model):
	time = models.DateTimeField()
	message = models.CharField(max_length=250)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.message