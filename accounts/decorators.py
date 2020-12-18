from django.http import HttpResponse
from django.shortcuts import redirect


#Don't Allow authenticated user to view login page
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func

#Group wise permission to view to page
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Sorry! Your are not allow to view this page')
        return wrapper_func
    return decorator
