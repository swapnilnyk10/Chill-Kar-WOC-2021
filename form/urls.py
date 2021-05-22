from django.urls import path
from . import views
from django.contrib import admin

# The code Below is for Django Header Customization
admin.site.site_header = "Developer-Swapnil's Administration"
admin.site.site_title = "Swapnil's Admin"
admin.site.index_title="Dashboard of Mr. Swapnil"
urlpatterns = [  
    path('', views.index),
    path('homepage.html', views.homepage,name='homepage'),
    path('doctor.html', views.doctor,name='doctor'),
    path('display.html/', views.display,name='display'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('check', views.check, name='check'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]