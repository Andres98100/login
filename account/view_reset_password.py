from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .models import CustomUser as User
from .utils import generate_token

class PasswordResetRequest(APIView):
    def post(self, request):
        email = request.data.get('email')
        if email:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'error': 'No user with this email'}, status=status.HTTP_404_NOT_FOUND)

            token = generate_token(user)
            send_mail(
                'Password Reset',
                f'Use this token to reset your password: {token}',
                'from@example.com',
                [email],
                fail_silently=False,
            )
            return Response({'message': 'Token sent to your email'}, status=status.HTTP_200_OK)
        return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
