from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.conf import settings
from .forms import UserCreationForm, UserUpdateForm
from appointment.forms import AppointmentUpdateForm
from .decorators import unauthenticated_user, allowed_users
from appointment.models import Appointment
from django.contrib.auth import get_user_model


User = get_user_model()


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='Customer')
            user.groups.add(group)

            messages.success(request, f'Account created for {username}!')
            return redirect('loginPage')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(request, email=email, password=password)

        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                first_name = request.user.first_name
                last_name = request.user.last_name
                messages.success(request, f'Welcome {first_name} {last_name}!')
                return redirect('index')
        
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('loginPage')
    
    else:
        return render(request, 'accounts/login.html')

@login_required
def logout_view(request):
    auth.logout(request)
    messages.info(request, 'You are Logout. Thank you for useing our site')
    return redirect('loginPage')

@login_required
@allowed_users(['Customer'])
def dashboard(request):
    user_appointment = Appointment.objects.order_by('-apply_date').filter(user_id=request.user.id, is_visited=False )

    context = {
        'appointment': user_appointment,
    }

    return render(request,'accounts/dashboard.html', context)

@login_required
@allowed_users(['Customer'])
def user_history(request):
    user_appointment = Appointment.objects.order_by('-apply_date').filter(user_id=request.user.id, is_visited=True )

    context = {
        'appointment': user_appointment,
    }

    return render(request,'accounts/user_history.html', context)

@allowed_users(['Customer'])
def visited(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    appointment.is_visited = True
    appointment.save()
    return redirect('dashboard')

@login_required
def view_profile(request, user_id):
    user_details = get_object_or_404(User,pk = user_id)

    context = {
        'user_details' : user_details
    }
    return render(request,'accounts/view_profile.html', context)

@login_required
def update_user_profile(request):
    if request.method == 'POST':
        u_updateForm = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if u_updateForm.is_valid():
            u_updateForm.save()
            messages.success(request, f'Your account has been update!')
            return redirect('user_profile')
    
    else:
        u_updateForm =UserUpdateForm(instance=request.user)

    context = {
        'form' : u_updateForm
    }
    return render(request,'accounts/user_profile.html', context)
