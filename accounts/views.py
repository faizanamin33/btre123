from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact



def signup(request):

    if request.method == 'POST':
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       password2 = request.POST['password2']

       if password == password2:
           if User.objects.filter(username=username).exists():
               messages.error(request, "Username already taken")
               return redirect('signup')
           else:
               if User.objects.filter(email=email).exists():
                   messages.error(request, "This email is already registered")
                   return redirect('signup')
               else:
                   user = User.objects.create_user(username=username, email=email, password=password,
                                            first_name=first_name, last_name=last_name)
                   user.save()
                   messages.success(request, 'Your account is created')
                   return redirect('login')
       else:
           messages.error(request, "Password do not match")
           return redirect('signup')

    else:
        return render(request, 'accounts/signup.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Now You are logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid usename or password')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def dashboard(request):

    user_contact = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts':user_contact
    }

    return render(request, 'accounts/dashboard.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are logout')
        return redirect('index')



