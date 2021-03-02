# myproject/apps/accounts/views.py
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserAvatarSerializer
from .utils import processImageInput
from django.core.files.storage import default_storage

class UserAvatarUpload(APIView):
    parser_classes = [MultiPartParser, FormParser, FileUploadParser]
#    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = UserAvatarSerializer(data=request.data, instance=request.user)
        
        
        if serializer.is_valid():
            #path = default_storage.save('temp_image.jpg', serializer.avatar)
            #processImageInput(path)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
