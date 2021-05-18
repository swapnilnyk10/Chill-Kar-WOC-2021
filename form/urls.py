from django.urls import path
from form import views
from django.contrib import admin

# The code Below is for Django Header Customization
admin.site.site_header = "Developer-Swapnil's Administration"
admin.site.site_title = "Swapnil's Admin"
admin.site.index_title="Dashboard of Mr. Swapnil"
urlpatterns = [  
    path('', views.index),
    path('homepage.html', views.homepage,name='homepage'),
    path('display.html', views.display,name='display'),
]