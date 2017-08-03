from django.contrib import admin

# Register your models here.
from sign.models import Event,Guest,Test

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'start_time','id']

class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone','email','sign','create_time','event']

class TestAdmin(admin.ModelAdmin):
    list_display = ['name', 'age',];

admin.site.register(Event,EventAdmin);
admin.site.register(Guest,GuestAdmin);
admin.site.register(Test,TestAdmin);