from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import GoalForm, ProgressForm
from django.contrib.auth.forms import UserCreationForm
from .models import Goal, Progress
from django.utils import timezone

@login_required
def home(request):
    goals = Goal.objects.filter(user=request.user) if request.user.is_authenticated else []
    return render(request, 'tracker/home.html', {'goals': goals})

@login_required
def create_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('home')
    else:
        form = GoalForm()
    return render(request, 'tracker/create_goal.html', {'form': form})

@login_required
def update_progress(request):
    if request.method == 'POST':
        form = ProgressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProgressForm()
    return render(request, 'tracker/update_progress.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/register.html', {'form': form})

@login_required
def update_progress(request):
    if request.method == 'POST':
        form = ProgressForm(request.POST)
        if form.is_valid():
            progress = form.save(commit=False)
            progress.user = request.user
            progress.date = timezone.now()  # Set the current date/time if required
            progress.save()
            return redirect('progress_success')  # Redirect to success page
    else:
        form = ProgressForm()

    return render(request, 'tracker/update_progress.html', {'form': form})

def progress_success(request):
    # Render a success page or message after progress update
    return render(request, 'tracker/progress_success.html')


