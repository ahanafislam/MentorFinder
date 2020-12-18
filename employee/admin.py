from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):

    list_display = ("employee_name","hire_date",)

    #Only admin have change permission
    def has_change_permission(self, request, obj=None, **kwargs):
        has = super().get_form(request, obj, **kwargs)
        is_admin = request.user.is_admin

        if not is_admin:
            return False

        return has

    #Only admin have add permission
    def has_add_permission(self, request, obj=None, **kwargs):
        has = super().get_form(request, obj, **kwargs)
        is_admin = request.user.is_admin

        if not is_admin:
            return False

        return has

    #Only admin have Delete permission
    def has_delete_permission(self, request, obj=None, **kwargs):
        has = super().get_form(request, obj, **kwargs)
        is_admin = request.user.is_admin

        if not is_admin:
            return False

        return has
            


admin.site.register(Employee, EmployeeAdmin)
