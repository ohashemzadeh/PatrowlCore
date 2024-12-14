from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiExample
from .serializers import MonitorModeSerializer


EXAMPLE_RESPONSE_ARTIFACTS = OpenApiExample(
    name='EXAMPLE_RESPONSE_ARTIFACTS',
    status_codes=["200"],
    response_only=True,
    value=[
        {
            "name": "Example Request",
            "value": {
                    "asset_name": "Server 1",
                    "product_name": "Firewall",
                    "vendor_name": "Vendor A"
            },
        }
    ],
)


class AddAssetsProductVendorView(APIView):
    @extend_schema(
        summary="Add assets, product, and vendor to monitor mode",
        description=(
            "This API allows you to add an asset, product,and vendor"
            "into monitor mode by providing their details."
        ),
        request=MonitorModeSerializer,  # Request body schema
        responses={
            200: MonitorModeSerializer,  # Response schema (or a description of the response)
            400: "Validation error",
        },
        examples=[EXAMPLE_RESPONSE_ARTIFACTS]
        # examples = {"a" : "v"}
        # examples=[
        #     {
        #         "name": "Example Request",
        #         "value": {
        #             "asset_name": "Server 1",
        #             "product_name": "Firewall",
        #             "vendor_name": "Vendor A"
        #         },
        #     }
        # ],
    )
    def post(self, request):
        serializer = MonitorModeSerializer(data=request.data)
        if serializer.is_valid():
            data = {
                "message": "Asset, product, and vendor added to monitor mode successfully.",
                "submitted_data": serializer.validated_data
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
