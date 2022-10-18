from django.db import models

# Create your models here.

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

class User(models.Model):
	# auto incrementing id is provided by Django by default
	# auto_increment_id = models.AutoField(primary_key=True)
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