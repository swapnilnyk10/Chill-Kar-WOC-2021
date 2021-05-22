from django.contrib import admin
from .models import collect
from .models import Room
from .models import Message
# Register your models here.
admin.site.register(collect)
admin.site.register(Room)
admin.site.register(Message)