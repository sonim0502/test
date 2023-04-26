from django.shortcuts import render
import requests
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def file_list(request):
    # Make a GET request to the API endpoint
    response = requests.get('http://127.0.0.1:6001/api/files/')
    
    # Get the JSON data from the response
    files = response.json()
    
    # Pass the data to the template context
    context = {'files': files}
    
    # Render the template with the context
    return render(request, 'view.html', context)

def view(request):
    return render(request,'view.html')

def home1(request):
    return render(request, 'profile.html')


def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile')  # profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
            form = AuthenticationForm()
            return render(request, 'login.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')


def signout(request):
    logout(request)
    return redirect('/')

def home(request):
    return render(request,'home.html')
