from django.urls import path
from django.contrib import admin
from .views import change_password, upload_profile_picture
from . import views

app_name = 'myapp'

urlpatterns=[
    path('admin/', admin.site.urls),
    path('change-password/', change_password, name='change_password'),
    path('upload-profile-picture/', upload_profile_picture, name='upload_profile_picture'),
   
]