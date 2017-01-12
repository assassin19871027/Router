from django.contrib import admin
from RouterWebsite.models import Device, Notification, Rule, Traffic, SSID
# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('username', 'domain', 'activity', 'visited')

admin.site.register(Device, DeviceAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('content',)

admin.site.register(Notification, NotificationAdmin)

class RuleAdmin(admin.ModelAdmin):
    list_display = ('content',)

admin.site.register(Rule, RuleAdmin)

class TrafficAdmin(admin.ModelAdmin):
    list_display = ('url',)

admin.site.register(Traffic, TrafficAdmin)

class SSIDAdmin(admin.ModelAdmin):
    list_display = ('ssid_name',)

admin.site.register(SSID, SSIDAdmin)