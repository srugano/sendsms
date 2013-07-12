from djfrom django.db import models

# Create your models here.

class Questions(models.Model):
	question=models.CharField(max_length=50)
	def __unicode__(self):
		return self.question

class History(models.Model):
	tel_num=models.CharField(max_length=20)
	question=models.CharField(max_length=50)
	response=models.CharField(max_length=50)
	status=models.IntegerField(default=0)
	def __unicode__(self):
		return self.tel_num
