from django.shortcuts import render,redirect

from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact

# Create your views here.

def contact(request):
   if request.method == 'POST':

       listing_id = request.POST['listing_id']
       listing = request.POST['listing']
       name = request.POST['name']
       email = request.POST['email']
       phone = request.POST['phone']
       message = request.POST['message']

       user_id = request.POST['user_id']
       realtor_email = request.POST['realtor_email']

       if request.user.is_authenticated:
           user_id = request.user.id
           has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
           if has_contacted:
               messages.error(request, 'You have already made an inquiry for this property')
               return redirect('/listings/' + listing_id)


       contact = Contact(listing = listing, listing_id= listing_id, name=name, email=email,
                         phone=phone, message=message, user_id=user_id)
       contact.save()

       #send Email

       send_mail('An inquiry for property: ' + listing,
                 'There is an email for your property listing kindly log in to admin pannel for further details',
                 'faizanamin33@gmail.com',
                 [realtor_email, 'faizan.tech7@gmail.com'],
                 fail_silently=False)

       messages.success(request, 'Your inquiry is submitted we will contact you shortly')

       return redirect('/listings/'+listing_id)