import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings


AI_URL = f"{settings.LLM_PROJECT_ADDR}/llm-api/"


@api_view(['POST'])
def ask_question_from_ai_view(request):
    """
    Accepts a question, forwards it to the AI service
    and returns the response from the AI service.
    """
    # Validate input
    if 'query' not in request.data:
        return Response({"error": "Query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

    query = request.data['query']

    # Send the request to the AI service

    ai_response = requests.post(AI_URL, json={"query": query})

    # Check if the request was successful
    if not status.is_success(ai_response.status_code):
        return Response(
            {"error": "Failed to get response from AI service."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return Response(ai_response.json(), status=status.HTTP_200_OK)
