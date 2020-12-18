from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logout_view, name='logout'),
    path("user_profile/", views.update_user_profile, name='user_profile'),
    path("<int:user_id>/", views.view_profile, name='view_profile'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("user_history/", views.user_history, name='user_history'),
    path("visited/<appointment_id>", views.visited, name='visited'),
]