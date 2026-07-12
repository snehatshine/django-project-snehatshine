from django.shortcuts import render,redirect
from .forms import UserProfileForm
from .models import UserProfile

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def register(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = UserProfileForm()
    return render(request, 'register.html', {'form': form})
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = UserProfile.objects.get(username=username,password=password)
            return redirect('/')
        except UserProfile.DoesNotExist:
            error = "Invalid Username or Password"
            return render(request, 'login.html', {'error': error})
    return render(request, 'login.html')