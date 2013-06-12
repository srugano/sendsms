from django.db import models
# Create your models here.
class User(models.Model):
    answear = models.BooleanField(default=True)
    first_name = models.CharField(blank=True, max_length=30, verbose_name='nom', )
    telephone = models.IntegerField(default=123456,verbose_name='telephone')
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.telephone)
    class Meta:
        ordering = ('first_name',)

class Questions(models.Model):
	import datetime
	now = datetime.datetime.now()
	numero = models.AutoField(primary_key=True)
	question = models.CharField(max_length=300)
	release_date = models.DateField(default=now)
	def __unicode__(self):
		return u'%d %s' % (self.numero, self.question)
	class Meta:
		ordering = ('release_date',)
		verbose_name_plural = "questions"
        
class Responses(models.Model):
	import datetime
	now = datetime.datetime.now()
	response = models.CharField(max_length=300 )
	release_date = models.DateField(default=now)
	question = models.ForeignKey(Questions)
	def __unicode__(self):
		return u'%s' % (self.response)
	class Meta:
		ordering = ('release_date',)
		verbose_name_plural = "reponses"
		
class States(models.Model):
	user = models.ForeignKey(User, verbose_name='Utilisateur')
	n_messages = models.IntegerField()
	ordre = models.IntegerField(default=0)
	def __unicode__(self):
		return u'%s %s' % (self.user, self.n_messages)
	class Meta:
		ordering = ('user',)
		verbose_name_plural = "states"
