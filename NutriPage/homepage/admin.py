from django.contrib import admin

from NutriPage.homepage.models import MissionStatement, ContactInformation


class MissionStatementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)  # Allows filtering by creation date
    ordering = ('-created_at',)  # Order by the latest created first

class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ('contact_type', 'details', 'created_at')
    search_fields = ('contact_type', 'details')
    list_filter = ('contact_type',)  # Allows filtering by contact type
    ordering = ('contact_type',)  # Order alphabetically by contact type

admin.site.register(MissionStatement, MissionStatementAdmin)
admin.site.register(ContactInformation, ContactInformationAdmin)