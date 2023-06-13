from django.shortcuts import render
from library.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail

# Create your views here.


def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to DevAl'
        message = 'Hope you are enjoying your Django Tutorials'
        recepient = str(sub['email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'registration/success.html', {'recepient': recepient})
    return render(request, 'registration/index.html', {'form':sub})