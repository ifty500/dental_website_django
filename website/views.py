from django.shortcuts import render
from django.core.mail import send_mail
import smtplib
import os

# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        context = {'message_name': message_name }

        send_mail(
            message_name,
            message,
            message_email,
            ['iftiyar500@gmail.com'],
            fail_silently=True,




        )


        return render(request, 'contact.html', context)


    else:
        return render(request, 'contact.html', {})
