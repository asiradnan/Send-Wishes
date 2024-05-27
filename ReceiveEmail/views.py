from django.core.mail import send_mail,get_connection,EmailMessage
from django.shortcuts import render 
from . import settings
from django.http import HttpResponse
def home(request):
    if request.method=="POST":
        subject = request.POST['subject']
        body = request.POST['body']
        to_list = request.POST['to'].split(',')
        bcc_list = request.POST['bcc'].split(',')
        file = request.FILES.get('file',None)
        if len(to_list)>0 and len(bcc_list)>0:
            email = EmailMessage(subject,body,settings.EMAIL_HOST_USER,to_list,bcc_list)
        elif len(to_list)>0:
            email = EmailMessage(subject,body,settings.EMAIL_HOST_USER,to_list)
        elif len(bcc_list)>0:
            email = EmailMessage(subject,body,settings.EMAIL_HOST_USER,[],bcc_list)
        if file is not None:
            email.attach(file.name, file.read(), file.content_type)
        x= email.send()
        if x==0:
            return HttpResponse("Error occured")
        return HttpResponse("Sent successfully!")
    return render(request,"home.html")
    