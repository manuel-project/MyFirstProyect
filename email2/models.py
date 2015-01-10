from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EmailFolder(models.Model):
    user = models.ForeignKey(User, null=True)
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class EmailContent(models.Model):
    reference = models.IntegerField()
    user = models.ForeignKey(User, null=True)
    issue = models.CharField(max_length=250)
    message = models.CharField(max_length=500)
    def __unicode__(self):
        return "%s (%s)"%(self.user.first_name,self.message)

class Email(models.Model):
    email_folder = models.ForeignKey(EmailFolder)
    email_content = models.ForeignKey(EmailContent)
    user = models.ForeignKey(User, null=True, related_name='e_user')
    important = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    date = models.DateField()
    
    def __unicode__(self):
        return important+" "+status+" "+date

class EmailAttach(models.Model):
    email_content = models.ForeignKey(EmailContent)
    patch = models.CharField(max_length=30)
    type_archive = models.CharField(max_length=8)
    url = models.CharField(max_length=100)
    def __unicode__(self):
        return patch+" "+type_archive+" "+url

