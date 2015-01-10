from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EmailFolder(models.Model):
    user = models.ForeignKey(User, null=True)
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class EmailContent(models.Model):
    user = models.ForeignKey(User)
    reference = models.IntegerField(max_length=10)
    issue = models.CharField(max_length=250)
    message = models.CharField(max_length=10000)
    def __unicode__(self):
        return "%s (%s)"%(self.issue,self.message)

class EmailOut(models.Model):
    email_folder = models.ForeignKey(EmailFolder)
    email_content = models.ForeignKey(EmailContent)
    user = models.ForeignKey(User, null=True)
    important = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    date = models.DateField(default=True)
    def __unicode__(self):
        return important+" "+status+" "+date

class EmailAttach(models.Model):
    email_content = models.ForeignKey(EmailContent)
    patch = models.CharField(max_length=30)
    type_archive = models.CharField(max_length=8)
    url = models.CharField(max_length=100)
    def __unicode__(self):
        return patch+" "+type_archive+" "+url

