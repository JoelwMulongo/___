# Routing

# APP URLS 
# create urls.py in app_name folder
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

url patterns = [ 
    path('posts', views.index, name='posts.index'),
    path('posts/create/', views.create, name='posts.create',
    path('posts/<int:id>/', views.show, name='posts.show'),
    path('posts/<int:id>/edit/', views.edit, name='posts.edit'),
    path('posts/<int:id>/delete/', views.delete, name='posts.delete'),
] 

# URL Route ex. names conventions
posts.index | posts.create | posts.edit | posts.delete | posts.show

# PROJECT URLS 
# Include the app urls into the project urls (project_name/urls.py) 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_name.urls'))
]

# Production Static route
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)