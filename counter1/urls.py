"""
URL configuration for counter1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
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
from django.conf import settings
from django.conf.urls.static import static

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) if settings.DEBUG else []

from django.contrib import admin
from django.urls import path
from task.views import render_up, render_calc, render_pausa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_up),
    path('pausa/', render_pausa ),
    path('calc/', render_calc ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) if settings.DEBUG else []