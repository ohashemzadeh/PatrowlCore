from rest_framework import serializers


class MonitorModeSerializer(serializers.Serializer):
    asset_name = serializers.CharField(max_length=100)
    product_name = serializers.CharField(max_length=100)
    vendor_name = serializers.CharField(max_length=100)


class AIQuestionAskingRequestSerializer(serializers.Serializer):
    session_id = serializers.CharField(max_length=255, required=True)
    query = serializers.CharField(required=True)


class AIQuestionAskingResponseSerializer(serializers.Serializer):
    session_id = serializers.ReadOnlyField()
    query = serializers.ReadOnlyField()
    message = serializers.ReadOnlyField()
    response = serializers.ReadOnlyField()
