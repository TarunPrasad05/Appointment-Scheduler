from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.


@login_required
def dashboard(request):   #main screen
    return render(request, 'registration/dashboard.html', {'section': 'dashboard'} )


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            #create new user but avoid saving
            new_user = user_form.save(commit=False)
            #set the password
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            #save user
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
        
    else:
        user_form = UserRegistrationForm()
    
    return  render(request, 'registration/register.html', {'user_form': user_form})


def book_appointment(request):
    return render(request, 'registration/book_appointment.html' )