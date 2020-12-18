from django.shortcuts import render
from accounts.decorators import allowed_users


@allowed_users(['Staff'])
def empDashboard(request):
    return render(request, "employee/empDashboard.html")
