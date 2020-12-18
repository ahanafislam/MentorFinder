from django.contrib import admin
from .models import Mentor


class MentorAdmin(admin.ModelAdmin):
    list_display = ('mentor_Name', 'title', 'catagory')
    search_fields = ["added_by", 'title', 'visiting_fees', 'catagory', 'district','name']
    list_filter = ('is_published', )
    ordering = ('join_date',)
    readonly_fields = [
        'added_by',
        'join_date',
        'name',
    ]

    def save_model(self, request, instance, form, change):
        username = request.user.username
        mentor_name = form.cleaned_data.get('mentor_Name')
        instance = form.save(commit=False)
        instance.added_by = username
        if instance.name is None:
            instance.name = mentor_name
        instance.save()
        form.save_m2m()
        return instance

admin.site.register(Mentor, MentorAdmin)
