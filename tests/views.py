from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):
    """
    A dummy view used only for testing.
    """

    def get(self, request):
        return Response({"msg": "Hello World!"}, status=status.HTTP_200_OK)
