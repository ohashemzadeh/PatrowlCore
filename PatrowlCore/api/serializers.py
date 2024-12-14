from rest_framework import serializers


class MonitorModeSerializer(serializers.Serializer):
    asset_name = serializers.CharField(max_length=100)
    product_name = serializers.CharField(max_length=100)
    vendor_name = serializers.CharField(max_length=100)
