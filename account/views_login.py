from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken

class UserLogin(ObtainAuthToken):
    # se usa super para llamar al metodo post de la clase padre
    def post(self, request, *args, **kwargs):
        response = super(UserLogin, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})

    # Otra forma de hacerlo mas explicita
    """ def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'detail': 'Inicio de sesión exitoso', 'token': token.key}) """