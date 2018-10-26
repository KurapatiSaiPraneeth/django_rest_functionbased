from rest_framework import serializers
from .models import snippet,LANGUAGE_CHOICES,STYLE_CHOICES

class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = snippet
        fields = ('id','title','code','linenos','language','style')



