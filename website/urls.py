
from django.contrib import admin
from django.urls import path,include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/',include('django.contrib.auth.urls')),
    #path('myapp/',include('myapp.urls')),
    path('myapp/', include('myapp.urls', namespace='myapp')),
    path('',views.Signup,name='signup'),
    path('login/',views.Login,name='login'),
    path('next/',views.Next,name='Next'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
