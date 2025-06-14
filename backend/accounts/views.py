from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomLoginForm, CustomUserCreationForm
from companies.models import Company
from django.utils.translation import gettext_lazy as _

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')  # username field contains email
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.get_full_name()}!')
                return redirect('accounts:dashboard')
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = CustomLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to your new account.')
            return redirect('accounts:dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user

    if user.is_parent:
        return redirect('companies:company_dashboard')
    elif user.is_admin or user.is_employee:
        return redirect('employees:employee_dashboard')
    else:
        messages.info(request, _("Welcome! Please register your company or contact your administrator."))
        return redirect('home')

@login_required
def email_change_view(request):
    # This is a placeholder view. Implement actual email change logic here.
    messages.info(request, "Email change functionality is not yet implemented.")
    return render(request, 'accounts/email_change.html') 