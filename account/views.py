from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import CustomUser as User

# Create your views here.
class UserRegistration(APIView):

    def get(self, request, id=None):
        if id is not None:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def deleteByID(self, id):
        user = User.objects.get(id=id)
        user.delete()
    
    def delete(self, request, id):
        self.deleteByID(id)
        return Response(status=status.HTTP_204_NO_CONTENT, data={'detail': 'Usuario eliminado'})