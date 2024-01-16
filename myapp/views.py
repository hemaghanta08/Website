from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import SignupForm
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def Signup(request):
    if request.method == 'POST':
        organization = request.POST.get('organization')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        mobile_number = request.POST.get('mobile_number')
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        data = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password1)
        data.save()

        return redirect('login')

    return render(request, 'signup.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('Next')

    return render(request, 'login.html')

def Next(request):
    return render(request, 'next.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login')  # Use the correct URL for redirection
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html')

@login_required
def upload_profile_picture(request):

    if request.method == 'POST':
        try:
            profile_pic = request.FILES['profile_picture']  
            logger.info("Got profile picture file")
            
            if profile_pic: 
                pic = request.user.profile_picture
                pic.save(profile_pic.name, profile_pic)
                logger.info("Profile picture uploaded!")

            return redirect('Next')

        except Exception as e:  
            logger.error("Error uploading profile picture", exc_info=True)
            return redirect('Next')

    else:
        return render(request, 'media/upload_profile_picture.html')