from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Mentor
from accounts.decorators import allowed_users
from mentors.choices import district_list,divisions_list, price_choices, category_list
from appointment.models import Appointment
from appointment.forms import AppointmentUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages


User = get_user_model()

def mentors_list(request):
    mentors = Mentor.objects.order_by('-join_date')
    
    paginator = Paginator(mentors,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'mentors' : paged_listings
    }
    return render(request,'mentors/mentors_list.html',context)

def mentors_details(request,mentor_id):
    mentors_details = get_object_or_404(Mentor,pk = mentor_id)

    context = {
        'mentors_details' : mentors_details
    }

    return render(request,'mentors/mentors_details.html',context)

def search(request):
    queryset_list = Mentor.objects.order_by('-join_date')

    #Search by keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(title__icontains=keywords)

    #Search by keywords
    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            queryset_list = queryset_list.filter(name__icontains=name)
    
    #Search by category
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            queryset_list = queryset_list.filter(catagory__iexact=category)

    #Search by Division
    if 'division' in request.GET:
        division = request.GET['division']
        if division:
            queryset_list = queryset_list.filter(divisions__iexact=division)

    #Search by district
    if 'district' in request.GET:
        district = request.GET['district']
        if district:
            queryset_list = queryset_list.filter(district__iexact=district)
    
    context = {
        'district_list' : district_list,
        'divisions_list' : divisions_list,
        'price_choices' : price_choices,
        'mentors' : queryset_list,
        'category' : category_list,
    }
    return render(request,'mentors/search.html',context)

@login_required
@allowed_users(['Mentor'])
def mentorDashboard(request):
    mentor = request.user.username
    user_appointment = Appointment.objects.order_by('-apply_date').filter(mentor_username=mentor, done_job=False)

    context = {
        'appointment': user_appointment,
    }
    return render(request,'mentors/mentorDashboard.html',context)

@login_required
@allowed_users(['Mentor'])
def mentorHistory(request):
    mentor = request.user.username
    user_appointment = Appointment.objects.order_by('-apply_date').filter(mentor_username=mentor, done_job=True)
    context = {
        'appointment': user_appointment,
    }
    return render(request,'mentors/mentor_history.html',context)

@login_required
@allowed_users(['Mentor'])
def done_job(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    appointment.done_job = True
    appointment.save()
    return redirect('mentorDashboard')

@login_required
@allowed_users(['Mentor'])
def appointmentDate(request, appointment_id):
    if request.method == "POST":
        appointment = Appointment.objects.get(pk=appointment_id)
        appointment.appointment_date = request.POST.get('appointment_date')
        appointment.save()
        return redirect('mentorDashboard')
