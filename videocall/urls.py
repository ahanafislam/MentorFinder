from django.urls import path
from videocall.views import video

app_name = 'videocall'

urlpatterns = [
    path('<streem_id>', video, name='video')
]