from django.shortcuts import render
from ArticleApi.models import Article
from ArticleApi.serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class api_View(APIView):

    def get(self,request):
        Articles = Article.objects.all()
        Serializer = ArticleSerializer(Articles, many=True)
        return Response(Serializer.data)

    def post(self,request):
        pass

