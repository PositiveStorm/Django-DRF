"""smart_home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from measurement.views import SensorView, SensorEdit, SensorMeasurement, MeasurementAdd

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/', SensorView.as_view()),
    path('sensors/<int:pk>/', SensorEdit.as_view()),
    path('sensors/info/<pk>/', SensorMeasurement.as_view()),
    path('measurements/', MeasurementAdd.as_view()),
]
