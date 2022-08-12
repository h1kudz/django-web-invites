from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Invites

class InvitesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'comment', 'created_at', 'updated_at',
                    'is_confirm')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'name')
    list_editable = ('is_confirm',)
    fields = ('name', 'comment', 'is_confirm', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Invites, InvitesAdmin)

admin.site.site_title = 'Управление приглашениями'
admin.site.site_header = 'Управление приглашениями'
