from django.contrib import admin
from email2.models import *
# Register your models here.
admin.site.register(EmailFolder)
admin.site.register(Email)
admin.site.register(EmailContent)
admin.site.register(EmailAttach)