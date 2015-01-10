from django.shortcuts import render, render_to_response
from email2.models import EmailFolder, EmailContent, Email, EmailAttach

# Create your views here.
def email_consultar(request):
    diccionary = {}
    import ipdb; ipdb.set_trace()
    diccionary['email_folder'] = EmailFolder.objects.all()
    diccionary['email_content'] = EmailContent.objects.all()
    diccionary['email'] = Email.objects.all()
    diccionary['email_attach'] = EmailAttach.objects.all()

    return render_to_response("index2.html", diccionary)