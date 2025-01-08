from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    # Get user's mood statistics
    mood_entries = request.user.mood_entries.all()
    total_entries = mood_entries.count()
    mood_distribution = {}
    if total_entries > 0:
        for mood_choice, _ in request.user.mood_entries.model.MOOD_CHOICES:
            count = mood_entries.filter(mood=mood_choice).count()
            percentage = (count / total_entries) * 100
            mood_distribution[mood_choice] = {
                'count': count,
                'percentage': round(percentage, 1)
            }

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'mood_stats': {
            'total_entries': total_entries,
            'mood_distribution': mood_distribution
        }
    }
    return render(request, 'accounts/profile.html', context)

def index(request):
    return render(request, 'index.html')
