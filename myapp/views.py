from django.shortcuts import render, redirect
from django.http import HttpResponse
from. forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = {
                'subject': form.cleaned_data['subject'],
                'name': form.cleaned_data['name'],
                'Email': form.cleaned_data['from_email'],
                'Message': form.cleaned_data['message']
            }
            from_mail = form.cleaned_data['from_email']
            message ="\n".join(body.values())

            try:
                send_mail(subject, message, from_mail, ['amoskoileken254@gmail.com'])
            except BadHeaderError:
                return HttpResponse('An error occured')
            messages.success(request, f'Message sent successfully! Will be in touch as soon as possible.')
            return redirect("contact")
      
    form = ContactForm()
    return render(request, "myapp/contact.html", {'form':form})

def services(request):
    return render(request, 'myapp/services.html')

def profile(request):
    return render(request, 'myapp/profile.html')

