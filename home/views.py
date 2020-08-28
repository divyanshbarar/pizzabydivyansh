from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(requests):
    return render(requests,"index.htm")

    #return HttpResponse("this is homepage")
def about(requests):
    return render(requests,"about.htm")

def services(requests):
    return render(requests,"services.htm")

def contact(requests):
    if requests.method == 'POST':
        name=requests.POST.get('name')
        email=requests.POST.get('email')
        phone=requests.POST.get('phone')
        desc=requests.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(requests, 'Profile details sumbitted!!!!!!!')

    return render(requests,"contact.htm")

