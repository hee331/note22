from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .seriarizers import DataSerializer, AccountSerializer
from django.http import Http404
from .models import data
from django.contrib.auth import authenticate, login, logout


class noteView(APIView):
    def get(self, pk):
        data = self.get_object(pk)
        serializer = DataSerializer(data)
        return Response(serializer.data)

class editView(APIView):
    def put(self, request, pk):
        data = self.get_object(pk)
        serializer = AccountSerializer(instance=data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        data = self.get_object(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class notepersonalView(APIView):
    def get(self,request):
        data = data.objects.all()
        serializer = DataSerializer(data, many=True)
        return Response(serializer.data)
    

class CreateUser(APIView):
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'ログイン成功'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'ログイン失敗'}, status=status.HTTP_401_UNAUTHORIZED)
        
class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'ログアウト成功'}, status=status.HTTP_200_OK)