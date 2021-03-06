from rest_framework import  status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import snippet
from .serializers import SnippetSerializer


@api_view(['GET','POST'])
def snippet_list(request, format=None):
    if request.method == 'GET':
        snippets = snippet.objects.all()
        serializer = SnippetSerializer(snippets, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def snippet_detail(request, pk, format=None):
    try:
        snippets = snippet.objects.get(pk=pk)
    except snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippets)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippets,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippets.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



