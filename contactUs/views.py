from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

# Create your views here.


def contact(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        message = request.POST['message']
        user_id = request.POST['user_id']

    contact = Contact(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number,
                      message=message, user_id=user_id)

    contact.save()
    messages.success(request, 'Submitted... Thanks for reaching out')
    return redirect('/')
