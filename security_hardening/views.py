from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from rest_framework import viewsets
from .models import SecurityCheck
from .serializers import SecurityCheckSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home_view(request):
    return render(request, 'internal/home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('internal/home.html')
        else:
            error_message = "Invalid credentials"
            return render(request, 'login.html', {'error': error_message})
    return render(request, 'login.html')

def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeatPassword = request.POST['repeatPassword']

        if password == repeatPassword:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                login(request, user)
                return redirect('/')
            except:
                error_message = "Username already exists"
                return render(request, 'signup.html', {'error': error_message})
        else:
            error_message = "Passwords do not match"
            return render(request, 'signup.html', {'error': error_message})
    return render(request, 'signup.html')

def user_logout(request):
    logout(request)
    return redirect('/login')

def demo_view(request):
    return render(request, 'external/demo.html')

def pricing_view(request):
    return render(request, 'external/pricing.html')

def contact_view(request):
    return render(request, 'external/contact.html')

def tools_view(request):
    return render(request, 'internal/tools.html')

def faq_view(request):
    return render(request, 'internal/faq.html')

def feedback_view(request):
    return render(request, 'internal/feedback.html')

# API views for SecurityCheck
class SecurityCheckViewSet(viewsets.ModelViewSet):
    queryset = SecurityCheck.objects.all()
    serializer_class = SecurityCheckSerializer

