from django.core.mail import EmailMessage
from django.shortcuts import render,redirect
from . import settings
from django.contrib import messages
def home(request):
    if request.method=="POST":
        subject = request.POST['subject']
        body = request.POST['body']
        to_list = request.POST['to'].split(',')
        bcc_list = request.POST['bcc'].split(',')
        file = request.FILES.get('file',None)
        try:
            email = EmailMessage(subject,body,settings.EMAIL_HOST_USER,to_list,bcc_list)
            if file is not None:
                email.attach(file.name, file.read(), file.content_type)
            email.send()
            messages.success(request,"Successfully sent the mail!")
        except:
            messages.error(request,"There was an sending the mail")
        return redirect("/")
        # if x==0:
        #     return HttpResponse("Error occured")
        # return HttpResponse("Sent successfully!")
    return render(request,"home.html")
    