from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, StaffLoginForm, PatientLoginForm, AdminLoginForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib import messages

# Role selection view
def select_role(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Handle form submission logic
            user = form.save()
            # Redirect to the login page
            return redirect('login')  # Use the correct name for the login URL
    else:
        form = CustomUserCreationForm()

    return render(request, 'select_role.html', {'form': form})

def staff_login(request):
    if request.method == 'POST':
        form = StaffLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to staff dashboard or any other staff-specific page
                return redirect('staff_dashboard')
    else:
        form = StaffLoginForm()
    
    return render(request, 'staff_login.html', {'form': form})

def patient_login(request):
    if request.method == 'POST':
        form = PatientLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            # Fetch user data from the database
         


            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.user = user  # Mark the user as authenticated
                    messages.success(request, 'Login successful')
                    # Fetch user data from the database
                    user_data = get_user_model().objects.filter(username=username).first()
                    # Redirect to patient dashboard with user data

                    return redirect('login/patient/dashboard', username=username)

                    

                else:
                    messages.error(request, 'Your account is not active.')
                    print(f"Authentication failed - Inactive user: {user}")
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
                print(f"Authentication failed - Username: {username}")
                return redirect('patient_login')  # Redirect back to the login page on authentication failure

        else:
            messages.error(request, 'Form is not valid. Please check the inputs.')
            print("Form is not valid. Please check the inputs.")
            return redirect('patient_login')  # Redirect back to the login page on form validation failure

    else:
        form = PatientLoginForm()

    return render(request, 'patient_login.html', {'form': form})


def patient_dashboard(request,username):
    user_data = get_user_model().objects.filter(username=username).first()
    return render(request, 'patient_dashboard.html', {'user_data': user_data})
    # return render(request, 'patient_dashboard.html')

def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')


def patient_logout(request):
    logout(request)
    return redirect('patient_login') 

def patient_signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirect to patient dashboard or any other patient-specific page
            return redirect('patient_dashboard')
    else:
        form = CustomUserCreationForm()

    return render(request, 'patient_signup.html', {'form': form})

def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to admin dashboard or any other admin-specific page
                return redirect('admin_dashboard')
    else:
        form = AdminLoginForm()


    return render(request, 'admin_login.html', {'form': form})

    return render(request, 'admin_login.html', {'form': form})



