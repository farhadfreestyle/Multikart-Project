from django.contrib import admin
from core.models import *
# Register your models here.
class SubscribersModelAdmin(admin.ModelAdmin):
    list_display = ['email']
    search_fields = ['email']
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ['questions','answers']
    search_fields = ['questions','answers']
class WorkersModelAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'image', 'position']
    search_fields = ['first_name','last_name', 'image', 'position']
class SendMessageModelAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'email', 'message']
    search_fields = ['first_name','last_name', 'email', 'message']
# Register your models here.
admin.site.register(Subscribers, SubscribersModelAdmin)
admin.site.register(Faq, FaqModelAdmin)
admin.site.register(Workers)
admin.site.register(SendMessage)