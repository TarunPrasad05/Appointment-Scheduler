from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages

# Create your views here.


@login_required
def dashboard(request):   #main screen
    user = request.user
    appointments = Appointment.objects.filter(user=user ).order_by('day', 'time')
    appointments2 = Appointment.objects.filter(user2=user ).order_by('day', 'time')
    appointment = appointments | appointments2
    return render(request, 'registration/dashboard.html', {
        'section': 'dashboard',
        'user':user,
        'appointments':appointment,
    } )


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



#new

def booking(request):
    #Calling 'validWeekday' Function to Loop days you want in the next 21 days:
    weekdays = validWeekday(7)

    #Only show the days that are not full:
    validateWeekdays = isWeekdayValid(weekdays)

    all_users= get_user_model().objects.all()
    all_users = all_users.exclude(username=request.user.username)

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')
        if service == None:
            messages.success(request, "Please Select A Terraformer!")
            return redirect('booking')
        if day == None:
            messages.success(request, "Please Select A Day!")
            return redirect('booking')

        #Store day and service in django session:
        request.session['day'] = day
        request.session['user2'] = service

        return redirect('bookingSubmit')


    return render(request, 'booking.html', {
            'weekdays':weekdays,
            'validateWeekdays':validateWeekdays,
            'allusers': all_users,
        })

def bookingSubmit(request):
    user = request.user
    times = [
        "10 AM","11 AM", "12 PM", "1 PM", "2 PM", "3 PM", "4 PM"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    #Get stored data from django session:
    day = request.session.get('day')
    user2 = request.session.get('user2')
    #Only show the time of the day that has not been selected before:
    hour = checkTime(times, day)
    if request.method == 'POST':
        time = request.POST.get("time")
        title = request.POST.get("title")
        agenda = request.POST.get("agenda")
        date = dayToWeekday(day)
        if time == None:
            messages.success(request, "Please Select A Time!")
            return redirect('bookingSubmit')

        if user2 != None:
            if day <= maxDate and day >= minDate:
                if  date != 'Saturday' and date != 'Sunday':
                    if Appointment.objects.filter(day=day).count() < 11:
                        if Appointment.objects.filter(day=day, time=time).count() < 1:
                            AppointmentForm = Appointment.objects.get_or_create(
                                user = user,
                                user2 = user2,
                                day = day,
                                time = time,
                                title = title,
                                agenda = agenda,
                            )
                            messages.success(request, "Appointment Saved!")
                            return redirect('booking')
                        else:
                            messages.success(request, "The Selected Time Has Been Reserved Before!")
                    else:
                        messages.success(request, "The Selected Day Is Full!")
                else:
                    messages.success(request, "The Selected Date Is Incorrect")
            else:
                    messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please Select A Terraformer!")


    return render(request, 'bookingSubmit.html', {
        'times':hour,
    })


def dayToWeekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y

def validWeekday(days):
    #Loop days you want in the next 21 days:
    today = datetime.now()
    weekdays = []
    for i in range (0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if  (y != 'Saturday' and y != 'Sunday'):
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays


def isWeekdayValid(x):
    validateWeekdays = []
    for j in x:
        if Appointment.objects.filter(day=j).count() < 10:
            validateWeekdays.append(j)
    return validateWeekdays

def checkTime(times, day):
    #Only show the time of the day that has not been selected before:
    x = []
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x

