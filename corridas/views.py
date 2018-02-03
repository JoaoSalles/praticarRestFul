# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

# Create your views here.



class crewQuestions(APIView):
    permission_classes = ()
    authentication_classes = ()
    renderer_classes = (JSONRenderer,)

    def get(self, request, format=None):
        return Response({}, status = status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    renderer_classes = (JSONRenderer,)
    # queryset = User.objects.all().order_by('-date_joined')
    # serializer_class = UserSerializer
    def list(self, request):
        return Response({}, status = status.HTTP_200_OK)


    def create(self, request):
        print 'entrou certo'
        return Response({}, status = status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        print str(pk) + 'aqui'
        return Response({}, status = status.HTTP_200_OK)