from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            send_mail(
                '[MyWebPage - Contact] Email from Django Contact Form', 
                data['message'] + '\n\n' + data['name'] + '\n' + data['email'] + '\n' + data['company'],
                None,
                ['sergifusterdura@gmail.com'],
                fail_silently=False,)
            
            return render(request, 'contact.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})