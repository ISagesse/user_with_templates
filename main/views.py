from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
    context = {
        'all_users': User.objects.all()
    }

    return render(request, 'index.html', context)

def create_user(request):
    first_name = request.POST['fName']
    last_name = request.POST['lName']
    your_email = request.POST['yEmail']
    your_age = request.POST['yAge']

    User.objects.create(name=f"{first_name} {last_name}", email=f"{your_email}", age=f"{your_age}")
    return redirect('/')