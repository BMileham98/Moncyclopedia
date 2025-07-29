from django.contrib import admin
from .models import Monster, Observation, Comment

# Register your models here.
admin.site.register(Monster)
admin.site.register(Observation)
admin.site.register(Comment)