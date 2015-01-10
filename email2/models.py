from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EmailFolder(models.Model):
    user = models.ForeignKey(User, null=True)
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Email(models.Model):
    email_folder = models.ForeignKey(EmailFolder)
    email_content = models.ForeignKey(EmailContent)
    user = models.ForeignKey(User, null=True)
    important = models.BooleanField()
    status = models.BooleanField()
    date = models.DateField()
    
    def __unicode__(self):
        return 

class EmailContent(models.Model):
    issue = models.CharField(max_length=250)
    message = models.ForeignKey(State)
    def __unicode__(self):
        return "%s (%s)"%(self.name,self.state)

class EmailAttach(models.Model):
    email_content = models.ForeignKey(EmailContent)
    patch = models.CharField(max_length=30)
    type_archive = models.CharField(max_length=8)
    url = models.CharField(max_length=100)
    def __unicode__(self):
        return patch+" "+type_archive+" "+url

