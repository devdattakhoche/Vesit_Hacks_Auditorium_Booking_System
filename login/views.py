from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from django.http import HttpResponse
from .models import Booking
import sys
import itertools


def loginpage(request):
    if request.method == 'POST':
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        print(Username)
        temp = Username
        user = authenticate(request, username=Username, password=Password)
        print(user)
        if user is not None:
            login(request, user)
            if Username == 'srajan':
              return redirect('/user_admin/')
            response = redirect('/Homepage/')
            return response
        else:
            failedresponse = redirect('/failed/')
            return failedresponse
        
    return render(request, 'login/loginpage.html')


def failed(request):
    return render(request, 'login/failed.html')


def success(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    hi = request.user.username
    params = {'pro': hi}
    print ("id:",request.user.id)
    return render(request, 'login/Homepage.html', params)


def loggedout(request):
    if request.user.is_authenticated and request.method == 'POST':
        logout(request)
    return render(request, 'login/loggedout.html')


@login_required
def booking(request):
    if 'userid' in request.POST or request.method == "POST":
        form = BookingForm(request.POST,request = request)
        if form.is_valid:
            Bookingform = form.save(commit=False)
            Bookingform.userid = request.user.id  # The logged-in user
            Bookingform.save()
            return redirect('/Requests/')
        else:
            return HttpResponse('invail form')
    form = BookingForm(request = request )
    return render(request, 'login/Booking.html',{'form' : form})

@login_required
def Requests(request):
    x=Booking.objects.filter(userid=request.user.id)
    params={'Object':x}
    print(x)
    return render(request, 'login/Requests.html',params)


@login_required
def History(request):
    return render(request, 'login/History.html')

def user_admin(request):
    return render(request, 'login/admin.html')

def Register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password)
        user.save()
        user = authenticate(request, username=username, password=password)
        login(request, user)
        response = redirect('/Homepage/')
        return response

    return render(request, 'login/register.html')
@login_required
def slots(request):
    x = Booking.objects.filter()
    k={  
        'pro':range(8,18),
        'book': x
    }
    return render(request, 'login/slots.html',k)
