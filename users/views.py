from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.core.mail import send_mail


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            messages.success(request, f'Account created for {username}!')

            # Register success
            # Send Email Comfirmation to that Account
            message = 'Hi new user,' \
                      'Thank you for creating an account at' \
                      'AirQualityMonitoringSystem Website.'
            send_mail(
                '[AirQualityMonitoringSystem] Welcome! ' + username, # subject
                message, # message
                'sakkarin.kmitl@gmail.com', # from email
                ['yougtin@gmail.com'], # to email
            )

            return redirect('/login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login(request):
    return render(request, 'users/login.html')