from rest_framework import serializers
from ArticleApi.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title','photo_Url','body','time']
