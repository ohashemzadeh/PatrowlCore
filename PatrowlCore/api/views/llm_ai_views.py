import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from ..serializers import AIQuestionAskingRequestSerializer, AIQuestionAskingResponseSerializer
from drf_spectacular.utils import extend_schema, OpenApiExample


@extend_schema(
    request=AIQuestionAskingRequestSerializer,
    responses={200: AIQuestionAskingResponseSerializer},
    description="Accepts a question and forwards it to the AI service. Returns the response from the AI service.",
    examples=[
        OpenApiExample(
            name="Example request",
            value={
                "session_id": "unique_session_123",
                "query": "What is CVSS?"
            },
            request_only=True,  # Example is only applicable for request
            response_only=False
        )
    ]
)
@api_view(['POST'])
def ask_question_from_ai_view(request):
    """
    Accepts a question, forwards it to the AI service
    and returns the response from the AI service.
    """

    serializer = AIQuestionAskingRequestSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)

    query = serializer.validated_data['query']
    session_id = serializer.validated_data['session_id']

    # Send the request to the AI service

    url = f"{settings.LLM_PROJECT_ADDR}/query"
    ai_response = requests.post(
        url,
        json={"query": query, "session_id": session_id},
        headers={"X-API-Key": settings.LLM_PROJECT_X_API_KEY}
    )

    return Response(ai_response.json(), status=ai_response.status_code)
