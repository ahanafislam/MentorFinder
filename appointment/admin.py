from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("mentor_Name", "name", "apply_date", "appointment_date","done_job", "is_visited")
    search_fields = ('name','mentor_Name', 'user_id')
    list_editable = ('is_visited',)
    list_filter = ("done_job", "is_visited", "appointment_date", "apply_date",)
    list_per_page = 25

    readonly_fields = [
        "mentor_title",
        "mentor_id",
        "mentor_Name",
        "mentor_category",
        "name",
        "email",
        "phone",
        "message",
        "apply_date",
        "user_id",
        "visiting_free",
        "done_job",
        "appointment_date",
    ]

admin.site.register(Appointment, AppointmentAdmin)
