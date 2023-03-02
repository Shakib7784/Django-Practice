from django.contrib import admin
from service.models import service, Contact

# Register your models here.

class serrviceAdmin(admin.ModelAdmin):
    list_display = ["service_icon","service_title","service_des"]

admin.site.register(service,serrviceAdmin)

class UserContact(admin.ModelAdmin):
    ld = ["name","email","password","address","city"]

admin.site.register(Contact,UserContact)