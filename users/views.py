from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib import messages
from django.views.generic import CreateView
from .models import Profile
from .forms import ProfileForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def dashboard(request):
    # if profile not created, redirect to create profile page
    if not Profile.objects.filter(user=request.user).exists():
        return redirect(reverse('create_profile'))
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            # save the user
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect(reverse('dashboard'))
        else:
            messages.error(request, 'Unsuccessful profile update. Invalid information.')
    form = ProfileForm(instance=request.user.profile)
    profile = Profile.objects.get(user=request.user)
    return render(request, 'users/dashboard.html', {'form': form, 'profile': profile})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # save the user
            user = form.save()
            # log the user in
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, 'Registration successful.')
            # if profile not created, redirect to create profile page
            if not Profile.objects.filter(user=user).exists():
                return redirect(reverse('create_profile'))
            else:
                return redirect(reverse('dashboard'))
        else:
            messages.error(request, 'Unsuccessful registration. Invalid information.')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # save the user
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profile created successfully.')
            return redirect(reverse('dashboard'))
        else:
            messages.error(request, 'Unsuccessful profile creation. Invalid information.')
    else:
        form = ProfileForm()
    return render(request, 'users/create_profile.html', {'form': form})

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            # save the user
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect(reverse('dashboard'))
        else:
            messages.error(request, 'Unsuccessful profile update. Invalid information.')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/update_profile.html', {'form': form})
