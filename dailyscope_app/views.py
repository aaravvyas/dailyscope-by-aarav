from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import News  # 👈 Import the News model
from .models import ContactMessage  # 👈 Import the ContactMessage model
from .forms import ContactForm  # 👈 Import the ContactForm (you will create this form)
from .forms import FeedbackForm  # ✅ Add this
from .models import News, Feedback 

# --- SIGNUP VIEW ---
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'dailyscope_app/signup.html', {'form': form})


# --- LOGIN VIEW ---
def login_view(request):
    error = None
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            error = "Invalid username or password"
    else:
        form = AuthenticationForm()
    return render(request, 'dailyscope_app/login.html', {'form': form, 'error': error})


# --- LOGOUT VIEW ---
def logout_view(request):
    logout(request)
    return redirect('login')


# --- HOME VIEW (loads news from DB using admin panel) ---
@login_required
def home_view(request):
    news_list = News.objects.order_by('-date')  # 👈 Latest news first
    return render(request, 'dailyscope_app/home.html', {'news_list': news_list})


# --- LOGOUT CONFIRMATION VIEW ---
@login_required
def logout_confirm_view(request):
    return render(request, 'dailyscope_app/logout_confirm.html')


# --- PROFILE VIEW ---
@login_required
def profile_view(request):
    user = request.user
    return render(request, 'dailyscope_app/profile.html', {'user': user})


# --- ABOUT US VIEW ---
@login_required
def about_view(request):
    return render(request, 'dailyscope_app/about.html')


# --- CONTACT US VIEW ---
@login_required
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'dailyscope_app/contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'dailyscope_app/contact.html', {'form': form})


# --- FEEDBACK VIEW ---
@login_required
def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('home')
    else:
        form = FeedbackForm()
    return render(request, 'dailyscope_app/feedback.html', {'form': form})