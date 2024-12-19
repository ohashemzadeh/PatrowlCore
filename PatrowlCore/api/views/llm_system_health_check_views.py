import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings


@api_view(['GET'])
def health_check_view(request):
    try:
        # Send a request to check the AI system
        ai_response = requests.get(f"{settings.LLM_PROJECT_ADDR}/", timeout=5)

        # Check if the response status is successful
        if ai_response.status_code >= 200 and ai_response.status_code < 300:
            return Response(
                {"data": "AI system is up and ready."},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"data": f"AI system responded with an issue. Status code: {ai_response.status_code}"},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

    except requests.exceptions.ConnectionError:
        return Response(
            {"data": "AI system is unreachable. Connection error occurred."},
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )
    except requests.exceptions.Timeout:
        return Response(
            {"data": "AI system did not respond in time. Request timed out."},
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )
    except requests.exceptions.RequestException as e:
        return Response(
            {"data": f"An error occurred while checking the AI system: {str(e)}"},
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )
