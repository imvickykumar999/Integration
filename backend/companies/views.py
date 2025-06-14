from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.db.models import Count
from .models import Company, Department
from .forms import CompanyRegistrationForm, AdminUserCreationForm, DepartmentForm
from accounts.models import User
from employees.models import Employee

def register_company(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            company = form.save()
            messages.success(request, _('Company registered successfully. Please check your email to verify your account.'))
            return redirect('accounts:account_login')
    else:
        form = CompanyRegistrationForm()
    return render(request, 'companies/register.html', {'form': form})

@login_required
def company_dashboard(request):
    if not request.user.is_parent:
        messages.error(request, _('Access denied. Only company owners can access this page.'))
        return redirect('home')
    
    try:
        company = Company.objects.get(owner=request.user)
    except Company.DoesNotExist:
        messages.info(request, _('Please register your company first.'))
        return redirect('companies:register')

    context = {
        'company': company,
        'admin_count': User.objects.filter(role=User.UserRole.ADMIN, company=company).count(),
        'employee_count': Employee.objects.filter(company=company).count(),
        'department_count': Department.objects.filter(company=company).count(),
    }
    return render(request, 'companies/dashboard.html', context)

@login_required
def admin_dashboard(request):
    if not request.user.is_admin:
        messages.error(request, _('Access denied. Only admin users can access this dashboard.'))
        return redirect('home')

    company = request.user.company # For admin users, company is directly linked to the user
    
    if not company:
        messages.error(request, _('Company not found or linked.'))
        return redirect('home')

    context = {
        'company': company,
        'employee_count': Employee.objects.filter(company=company).count(),
        'department_count': Department.objects.filter(company=company).count(),
        'admin_count': User.objects.filter(role=User.UserRole.ADMIN, company=company).count(),
        # Add other admin-specific context here
    }
    return render(request, 'companies/admin_dashboard.html', context)

@login_required
def admin_users(request):
    if not request.user.is_parent:
        messages.error(request, _('Access denied. Only company owners can access this page.'))
        return redirect('home')
    
    company = get_object_or_404(Company, owner=request.user)
    admin_users = User.objects.filter(role=User.UserRole.ADMIN, company=company)
    
    if request.method == 'POST':
        form = AdminUserCreationForm(request.POST)
        if form.is_valid():
            admin_user = form.save(company=company)
            messages.success(request, _('Admin user created successfully.'))
            return redirect('companies:admin_users')
    else:
        form = AdminUserCreationForm()
    
    context = {
        'company': company,
        'admin_users': admin_users,
        'form': form,
    }
    return render(request, 'companies/admin_users.html', context)

@login_required
def company_profile(request):
    if not request.user.is_parent:
        messages.error(request, _('Access denied. Only company owners can access this page.'))
        return redirect('home')
    
    company = get_object_or_404(Company, owner=request.user)
    
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, _('Company profile updated successfully.'))
            return redirect('company_profile')
    else:
        form = CompanyRegistrationForm(instance=company)
    
    context = {
        'company': company,
        'form': form,
    }
    return render(request, 'companies/profile.html', context)

@login_required
def delete_admin_user(request, user_id):
    if not request.user.is_parent:
        messages.error(request, _('Access denied. Only company owners can perform this action.'))
        return redirect('home')
    
    admin_user = get_object_or_404(User, id=user_id, role=User.UserRole.ADMIN)
    if request.method == 'POST':
        admin_user.delete()
        messages.success(request, _('Admin user deleted successfully.'))
    return redirect('admin_users')

@login_required
def department_list(request):
    if not (request.user.is_admin or request.user.is_parent):
        messages.error(request, _('Access denied. Only company owners and admin users can manage departments.'))
        return redirect('home')
    
    if request.user.is_parent:
        company = Company.objects.get(owner=request.user)
    else:
        company = request.user.company
    
    if not company:
        messages.error(request, _('Company not found or linked.'))
        return redirect('home')

    departments = Department.objects.filter(company=company)
    context = {
        'company': company,
        'departments': departments
    }
    return render(request, 'companies/department_list.html', context)

@login_required
def add_department(request):
    if not (request.user.is_admin or request.user.is_parent):
        messages.error(request, _('Access denied. Only company owners and admin users can add departments.'))
        return redirect('home')

    if request.user.is_parent:
        company = Company.objects.get(owner=request.user)
    else:
        company = request.user.company

    if not company:
        messages.error(request, _('Company not found or linked.'))
        return redirect('home')

    if request.method == 'POST':
        form = DepartmentForm(request.POST, company=company)
        if form.is_valid():
            form.save()
            messages.success(request, _('Department added successfully.'))
            return redirect('companies:department_list')
    else:
        form = DepartmentForm(company=company)
    
    context = {
        'company': company,
        'form': form
    }
    return render(request, 'companies/add_department.html', context)

@login_required
def edit_department(request, department_id):
    if not (request.user.is_admin or request.user.is_parent):
        messages.error(request, _('Access denied. Only company owners and admin users can edit departments.'))
        return redirect('home')

    if request.user.is_parent:
        company = Company.objects.get(owner=request.user)
    else:
        company = request.user.company

    if not company:
        messages.error(request, _('Company not found or linked.'))
        return redirect('home')

    department = get_object_or_404(Department, id=department_id, company=company)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department, company=company)
        if form.is_valid():
            form.save()
            messages.success(request, _('Department updated successfully.'))
            return redirect('companies:department_list')
    else:
        form = DepartmentForm(instance=department, company=company)
    
    context = {
        'company': company,
        'form': form,
        'department': department
    }
    return render(request, 'companies/edit_department.html', context)

@login_required
def delete_department(request, department_id):
    if not (request.user.is_admin or request.user.is_parent):
        messages.error(request, _('Access denied. Only company owners and admin users can delete departments.'))
        return redirect('home')

    if request.user.is_parent:
        company = Company.objects.get(owner=request.user)
    else:
        company = request.user.company

    if not company:
        messages.error(request, _('Company not found or linked.'))
        return redirect('home')

    department = get_object_or_404(Department, id=department_id, company=company)
    if request.method == 'POST':
        department.delete()
        messages.success(request, _('Department deleted successfully.'))
        return redirect('companies:department_list')
    
    context = {
        'company': company,
        'department': department
    }
    return render(request, 'companies/delete_department.html', context) # You might want a confirmation page for deletion. 