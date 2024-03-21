from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, send_mail
from .forms import ContactForm
from django.conf import settings
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        error = {}
        form = ContactForm(request.POST)
        error['form'] = form
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = f'New contact {email}: {name}'

            send_mail(subject, message, settings.CONTACT_EMAIL, settings.ADMIN_EMAILS)
            return render(request, 'contact/success.html')

    form = ContactForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'home/index.html', context)


