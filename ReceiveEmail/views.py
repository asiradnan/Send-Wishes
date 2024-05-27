from django.core .mail import send_mail
from django.shortcuts import render 
from . import settings
from django.http import HttpResponse
def home(request):
    if request.method=="POST":
        subject = request.POST['subject']
        body = request.POST['body']
        email = request.POST['email']
        x = send_mail(subject,body,settings.EMAIL_HOST,[email])
        if (x==1):
            return HttpResponse("Email sent successfully!")
        return HttpResponse("Error")
    return render(request,"home.html")
    