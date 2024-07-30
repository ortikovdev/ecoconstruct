from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="mvphome"),
    path('emarket/', views.emarket, name="emarket"),
    path('trashremoving/', views.trashremoving, name="trashremoving"),
    path('proclean/', views.proclean, name="proclean"),
    path('aisolution/', views.aisolution, name="aisolution"),

]
