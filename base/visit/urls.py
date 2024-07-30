from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('mvphome/', include('construct.urls')),
    path('videorolik/', views.videorolik, name="videorolik")

]
