from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Message
from .forms import MessageForm
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def resume(request):
    return render(request, 'resume.html')


def services(request):
    return render(request, 'services.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def contact(request):
    model = Message.objects.all()
    if request.method == 'POST':
        forms = MessageForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Your message has been sent')
            return redirect('contact')

    else:
        forms = MessageForm()

    context = {
        "model": model,
        "forms": forms
    }
    return render(request, 'contact.html', context)


def service_details(request):
    return render(request, 'services-details.html')


def download_resume(request):
    resume_file = 'media/resume/new_resume.pdf'
    with open(resume_file, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
        return response