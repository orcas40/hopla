from django.contrib import admin
from tickets.models import ticket
from tickets.models import ticket_image

@admin.register(ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id_ticket', 'ticket_description', 'num_images', 'status', 'created_at']


@admin.register(ticket_image)
class TicketImageAdmin(admin.ModelAdmin):
    list_display = ['id_image', 'id_ticket', 'url', 'created_at']
