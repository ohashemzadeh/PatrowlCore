from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MonitorModeSerializer

class AddAssetsProductVendorView(APIView):
    def post(self, request):
        serializer = MonitorModeSerializer(data=request.data)
        if serializer.is_valid():
            # Sample data to return
            data = {
                "message": "Asset, product, and vendor added to monitor mode successfully.",
                "submitted_data": serializer.validated_data
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)