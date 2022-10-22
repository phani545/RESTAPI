from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers  import *
from .models import *


# Create your views here.
@api_view(['GET'])
def Booklist(request):
    #return 'view'
    Articles = Article.objects.all()
    serializer = ArticleSerializer(Articles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_Book(request):
    Articles = Article.objects.all()
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)