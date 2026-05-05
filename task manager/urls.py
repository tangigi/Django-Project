"""
URL configuration for taskmanager project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Task_Manager.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Task_Manager/', add_task, name='task'),
    path('Task_Manager/delete/<int:id>/', delete, name='delete_task'),
    path('Task_Manager/edit/<int:id>/', edit_task, name='edit_task'),
    path('Task_Manager/reg', reg_task, name='register'),
    path('Task_Manager/login', login_task, name='login'),
    path('logout', logout_page, name='logout'),
    ]
