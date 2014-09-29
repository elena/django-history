# -*- coding: utf-8 -*-
from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .. import serializers
from lore.models import Talk


class TalkDetailAPI(APIView):

    def get_object(self, pk):
        try:
            return Talk.objects.get(pk=pk)
        except Talk.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if not pk:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        talk = self.get_object(pk)
        serializer = serializers.TalkSerializer(talk)
        return Response(serializer.data)

    def put(self, request, format=None):
        serializer = serializers.TalkCategorySerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
