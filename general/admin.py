from django.contrib import admin
from .models import MaintenanceEquipment, MaintenanceRequest, RecordEquipment
from django.urls import path
from django.http import HttpResponseRedirect

admin.site.site_header = "Admin dashboard"


class MaintenanceEquipmentAdmin(admin.ModelAdmin):
    list_display = ('category', 'image_Url')


class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('hostel', 'category', 'progress', 'remark')
    # list_filter = ('created',)


class RecordAdmin(admin.ModelAdmin):
    list_display = ('category', 'created', 'remark')
    # list_filter = ('created',)
    # change_list_template = 'snippets_change_list.html'

    # def get_urls(self):
    #     urls = super().get_urls()
    #     custom_urls = [
    #         path('fontsize/<int:size>/', self.change_font_size)
    #     ]
    #     return custom_urls + urls
    #
    # def change_font_size(self, request, size):
    #     self.model.objects.all().update(font_size=size)
    #     self.message_user(request, 'font size set successfully')
    #     return HttpResponseRedirect("../")


admin.site.register(MaintenanceEquipment, MaintenanceEquipmentAdmin)
admin.site.register(MaintenanceRequest, MaintenanceAdmin)
admin.site.register(RecordEquipment, RecordAdmin)
