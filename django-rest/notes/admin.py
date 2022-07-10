from django.contrib import admin

from . import models


class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "creation_date", "creation_time", "owner", "is_active")


admin.site.register(models.Note, NoteAdmin)
