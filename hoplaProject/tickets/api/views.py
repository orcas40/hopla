from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tickets.models import ticket, ticket_image
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from tickets.api.serializers import TicketSerializer, TicketImageSerializer
from rest_framework.pagination import PageNumberPagination
from datetime import datetime


import cloudinary.uploader

class MyPagination(PageNumberPagination):
    page_size = 10  # Número de elementos por página
    page_size_query_param = 'page_size'  # Parámetro opcional para especificar el tamaño de la página
    max_page_size = 100

class TicketApiView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    def get(self, request):
        user = request.user
        queryset = ticket.objects.filter(user=user.id)

        fecha_inicio = self.request.query_params.get('fecha_inicio', None)
        fecha_fin = self.request.query_params.get('fecha_fin', None)

        fecha_inicio = datetime.fromisoformat(fecha_inicio)
        fecha_fin = datetime.fromisoformat(fecha_fin)

        if fecha_inicio and fecha_fin:
            queryset = queryset.filter(created_at__range=[fecha_inicio, fecha_fin])

        status = self.request.query_params.get('status', None)
        if status:
            queryset = queryset.filter(status=status)

        # Paginar los resultados
        pagination_class = MyPagination
        # Paginar los resultados
        paginator = pagination_class()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = TicketSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        request.data['user'] = request.user.id
        ticket.objects.create(ticket_description=request.data['ticket_description'], num_images=request.data['num_images'], status=request.data['status'], user=request.data['user'])
        return self.get(request)

class TicketDetailApiView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    def get(self, request, id_ticket):
        user = request.user
        queryset = ticket.objects.filter(user=user.id)
        queryset = queryset.get(id_ticket=id_ticket)

        serializer = TicketSerializer(queryset)
        return Response(serializer.data)
class TicketImageApiView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if 'image' not in request.FILES:
            return Response({'error': 'No se ha proporcionado ninguna imagen'}, status=status.HTTP_400_BAD_REQUEST)

        uploaded_image = request.FILES['image']

        id_ticket = int(request.data['id_ticket'])
        upload_images_count = ticket_image.objects.filter(id_ticket=id_ticket).count()
        ticket_selected = ticket.objects.get(id_ticket=id_ticket)
        num_images_total = ticket_selected.num_images

        try:
            if ticket_selected.status != "completado":
                upload_response = cloudinary.uploader.upload(uploaded_image)
                if 'secure_url' in upload_response:
                    url_secure = upload_response['secure_url']
                    ticket_image.objects.create(id_ticket=ticket_selected, url=url_secure)
                    upload_images_count = upload_images_count + 1

                    if int(num_images_total) == upload_images_count:
                        ticket_selected.status = "completado"
                        ticket_selected.save()

                # Devuelve la URL pública de la imagen subida
                return Response({'image_url': upload_response['secure_url']}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Todas las imagenes para ese ticket estan completas'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error upload': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
