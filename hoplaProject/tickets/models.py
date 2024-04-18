from django.db import models
class ticket(models.Model):
    id_ticket = models.AutoField(primary_key=True)
    ticket_description = models.CharField(max_length=255)
    num_images = models.IntegerField(default=0)
    status = models.CharField(max_length=25, default="Pendiente")
    user = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class ticket_image(models.Model):
    id_image = models.AutoField(primary_key=True)
    id_ticket = models.ForeignKey( ticket, on_delete=ticket, null=True)
    url = models.URLField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)