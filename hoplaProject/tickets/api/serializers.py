from rest_framework.serializers import ModelSerializer
from tickets.models import ticket
from tickets.models import ticket_image

class TicketSerializer(ModelSerializer):
    class Meta:
        model = ticket
        fields = ['id_ticket', 'ticket_description', 'num_images', 'status', 'user', 'created_at']

class TicketImageSerializer(ModelSerializer):
    class Meta:
        model =  ticket_image
        fields = ['id_image', 'id_ticket', 'url', 'created_at']
