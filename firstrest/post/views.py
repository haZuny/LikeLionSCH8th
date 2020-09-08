#from django.shortcuts import render
from .models import Post
from .serializer import PostSerializer  #모델폼 비슷한거
from rest_framework import viewsets

# Create your views here.

#CBV로 작성

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#데이터 처리
from post.models import Post
from post.serializer import PostSerializer

#status에 따라 직접 response 처리
from django.http import Http404 #get gobject 구현
from rest_framework.response import Response
from rest_framework import status

#APIView를 상속받은 CBV
from rest_framework.views import APIView


#객체 목록을 보여줌
class PostList(APIView):
    #정보를 가져옴
    def get(self, request):
        posts = Post.objects.all()  #모든 객체를 가져옴
        serializer = PostSerializer(posts, many=True)   #객체를 serialize시킴
        return Response(serializer.data)    #데이터를 response

    #새로운 객체 등록
    def post(self, request):
        serializer = PostSerializer(data=request.data) #직렬화
        if serializer.is_valid():   #유효성 검사
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #Response(데이터, status, ...)


#PostList와 다르게 pk값을 받음
class PostDtail(APIView):
    #get_object_or_404;;;
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:   #pk가 존재하지 않을경우
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)  #get_object_or_404;;;
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data) #직렬화
        if serializer.is_valid():   #유효성 검사
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)