from datetime import datetime
from urllib.parse import urljoin

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemIdSerializer
from .utils import generate_pdf, generate_qr_code


class CashMachineView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ItemIdSerializer(data=request.data)
        if serializer.is_valid():
            item_ids = serializer.validated_data['items']
            items = Item.objects.filter(id__in=item_ids)

            if len(items) != len(item_ids):
                return Response({"error": "One or more items not found."}, status=status.HTTP_404_NOT_FOUND)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            pdf_filename = f'receipt_{timestamp}.pdf'
            qr_filename = f'qr_code_{timestamp}.png'

            pdf_path = generate_pdf(items, pdf_filename)
            pdf_url = urljoin(request.build_absolute_uri('/media/'), pdf_filename)

            qr_path = generate_qr_code(pdf_url, qr_filename)
            qr_url = urljoin(request.build_absolute_uri('/media/'), qr_filename)

            return Response({'qr_url': qr_url}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
