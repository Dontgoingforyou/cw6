from django.contrib import admin

from mailing_service.models import Mailing, Attempt


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_datetime', 'periodicity', 'status', 'message')
    list_filter = ('periodicity', 'status')
    filter_horizontal = ('clients',)


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ('id', 'mailing', 'attempt_datetime', 'status')
    list_filter = ('status',)
    search_fields = ('mailing__id',)
