from django.urls import path
from . import views
urlpatterns = [
    path('', views.mentors_list, name='mentors_list'),
    path('<int:mentor_id>/', views.mentors_details, name='mentors_details'),
    path('search/', views.search, name="search"),
    path('mentorDashboard/', views.mentorDashboard, name='mentorDashboard'),
    path('mentorHistory/', views.mentorHistory, name='mentorHistory'),
    path('done/<appointment_id>', views.done_job, name='done'),
    path('appointmentDate/<appointment_id>', views.appointmentDate, name='appointmentDate'),
]
