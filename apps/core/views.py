from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import authentication, permissions


class Protected(APIView):
    """
    View to responds an user data with authenticated permission
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return 200 status code with user data serialized
        """
        serializer = {
            "id": request.user.id,
            "email": request.user.email,
            "profile_id": request.user.profile_id,
            "identity_id": request.user.identity_id,
        }
        return Response(serializer, status=status.HTTP_200_OK)
