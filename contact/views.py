from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from decouple import config


# Create your views here.
def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            contact_email = form.cleaned_data['contact_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, contact_email, [config('MAIL_TO')])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'contact.html', {'form': form})


def success(request):
    return render(request, 'success.html')