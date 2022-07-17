from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, "authentication/index.html")
@csrf_exempt
def signup(request):

    if request.method == "POST":
        username = request.POST['email']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        user = User.objects.create_user(username,email, pass1)
        user.first_name = firstName
        user.last_name = lastName

        user.save()

        messages.success(request, "Account Successfully Created!")

    return render(request, "authentication/signup.html")


@csrf_exempt
def signin(request):

    if request.method =='POST':
        username = request.POST['email']
        pass1 = request.POST['password']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
        
        else:
            messages.error(request, "Invalid Email & Password")

    return render(request, "authentication/signin.html")

def signout(request):
    pass