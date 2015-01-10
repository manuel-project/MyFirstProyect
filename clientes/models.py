from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Country(models.Model):
	name = models.CharField(max_length=50)
	def __unicode__(self):
	    return self.name

class State(models.Model):
	name = models.CharField(max_length=50)
	country = models.ForeignKey(Country)
	def __unicode__(self):
	    return "%s - %s"%(self.name,self.country)

class City(models.Model):
	name = models.CharField(max_length=50)
	state = models.ForeignKey(State)
	def __unicode__(self):
	    return "%s (%s)"%(self.name,self.state)

class Clientes(models.Model):
	user = models.OneToOneField(User, unique=True)
	phone = models.IntegerField(max_length=8)
	address = models.TextField(max_length=100)
	city = models.ForeignKey(City)
	def __unicode__(self):
		return '%s (%s - %s)'%(self.user,self.city)


