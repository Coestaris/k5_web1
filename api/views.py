from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import URLSerializer
from .models import URL


class URLView(viewsets.ViewSet, GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = URLSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['creator'] = request.user
            serializer.save()
            return JsonResponse(serializer.data)
        return Response(status=400)

    def get(self, request, id):
        url = URL.objects.get(id=id)
        serializer = self.serializer_class(url)
        return JsonResponse(serializer.data, status=200)

    def put(self, request, id):
        user = request.user
        data = request.data
        url = URL.objects.filter(id=id).first()
        if url is None:
            return Response(status=404)
        serializer = self.serializer_class(url, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return Response(status=400)

    def delete(self, request, id):
        url = URL.objects.get(id=id)
        if url is None:
            return Response(status=404)
        url.delete()
        return Response(status=204)
