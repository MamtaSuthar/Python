from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),
    
    path('addmembers', views.addmembers, name='addmembers'),
    path('members/<int:id>/', views.members, name='members'),

    path('view_members/<int:id>/', views.view_members, name='view_members'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)