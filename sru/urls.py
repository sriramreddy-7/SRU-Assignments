"""
URL configuration for sru project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from assignments import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('post_assignment/', views.post_assignment,name='post_assignment'),
    path('login/', views.login,name='login'),
    path('admin_dashboard/', views.admin_dashboard,name='admin_dashboard'),
    path('<str:course_name>/', views.assigments_display,name='assigments_display'),
    path("post_assignment/", views.post_assignment, name="post_assignment"),
    path('faculty/', views.faculty, name='faculty'),
    path('update_assignment/<int:id>/', views.update_assignment, name='update_assignment'),
    path('delete_assignment/<int:id>/', views.delete_assignment, name='delete_assignment'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)