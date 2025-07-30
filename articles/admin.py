from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Monster, Observation, Comment


# Register your models here.
admin.site.register(Comment)

@admin.register(Monster)
class MonsterAdmin(SummernoteModelAdmin):
    list_display = ('id', 'name', 'category', 'founder', 'created_on')
    search_fields = ['name', 'description']
    list_filter = ('category', 'founder', 'created_on')
    summernote_fields = ('description',)

@admin.register(Observation)
class ObservationAdmin(SummernoteModelAdmin):
    list_display = ('id', 'title', 'monster', 'observer', 'observation_date')
    search_fields = ['title', 'observed_behaviour']
    list_filter = ('monster', 'observer', 'observation_date', 'danger_rating')
    summernote_fields = ('observed_behaviour', 'additional_notes')
    prepopulated_fields = {'slug': ('title',)} 