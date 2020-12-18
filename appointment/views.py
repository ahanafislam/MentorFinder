from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Appointment
from django.contrib.auth.decorators import login_required
from mentors.models import Mentor


@login_required
def appointment(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        mentor_id = request.POST['mentor_id']
        visiting_free = request.POST['visiting_free']
        mentor_Name = request.POST['mentor_Name']
        category = request.POST['category']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        # message = request.POST['message']
        mentor_username = request.POST['mentorUsername']

        # Check if user has already mande an appointment
        user_id = request.user.id
        has_appointment = Appointment.objects.all().filter(mentor_id=mentor_id, user_id=user_id, is_visited=False)

        if has_appointment:
            messages.error(request, 'You have already booked an appointment for this mentor')
            return redirect('/mentors/' + mentor_id)

        appointment = Appointment(user_id = user_id, mentor_id = mentor_id, visiting_free = visiting_free, mentor_Name = mentor_Name, mentor_category = category, name = name, email = email, phone = phone, mentor_username = mentor_username)
        appointment.save()

        messages.success(request, 'Your request has been submitted, our mentor will get back to you soon.')
        return redirect('/mentors/' + mentor_id)
    
    else:
        return redirect("mentors_list")

