from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets

from profiles_api import serializers

from profiles_api import models, permissions

from rest_framework.authentication import TokenAuthentication

class HelloApiView(APIView):
    """Test API View"""

    serializer_class= serializers.HelloSerializer

    def get(self, request, format=None):
        """Return list of APIView features"""
        an_apiview = [
            'uses HTTP methods as function(get,post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',

        ]

        return Response ({'message': 'Hello!','an_apiview': an_apiview})


    def post(self, request):
        """create a hello message with our name"""
        serializer= self.serializer_class(data=request.data)

        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            message= f'Hello {name}'
            return Response({'message': message})

        else:

            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )



    def put(self, request, pk=None):
        """handle updating an object"""
        return Response({'method':'PUT'})


    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Handle deleting an object"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API VIEWSETS"""
    serializer_class= serializers.HelloSerializer

    def list(self,request):
        """return a hello msg"""

        a_viewset=[
            'Uses Actions (list, create, retrieve,update,partial_update)',
            'Automatically maps to urls using routers',
            'provides more functionality with less code',
        ]

        return Response ({'message':'Hello', 'a_viewset':a_viewset})

    def create(self, request):
            """create a new hello msg"""

            serializer= self.serializer_class(data=request.data)

            if serializer.is_valid():
                name=serializer.validated_data.get('name')

                message= f'Hello {name}!'

                return Response ({'message':message})

            else:
                return  Response(

                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST

                )

    def retrieve(self,request,pk=None):
            """handle getting an object by its ID"""

            return Response({'http_metod':'GET'})

    def update(self,request,pk=None):
            """handle updating an object"""
            return Response({'http_metod':'PUT'})

    def partial_update(self,request, pk=None):
            """handle updating part of an object"""

            return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
            """handle removing an object"""

            return Response ({'http_method': 'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""


    serializer_class= serializers.UserProfileSerializer
    queryset= models.UserProfile.objects.all()
    authentication_classes= (TokenAuthentication,)
    permission_classes= (permissions.UpdateOwnProfile,)
