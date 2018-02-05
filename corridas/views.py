# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime
from models import *

# Create your views here.



class passageiroView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    renderer_classes = (JSONRenderer,)
    # queryset = User.objects.all().order_by('-date_joined')
    # serializer_class = UserSerializer
    def list(self, request):
        return Response({}, status = status.HTTP_200_OK)


    def create(self, request):
        result = {}
        result["success"] = False
        data = request.data
        date = datetime.strptime(data["date"], "%Y-%m-%d").date()
        cpf_treated = str(data["cpf"].replace(".","").replace("-",""))
        print 'entrou'
        try:
            Passageiro.objects.create(
            nome = str(data["nome"]),
            data_nascimento = date,
            cpf = cpf_treated,
            sexo = str(data["sexo"])
            )
        except Exception:
            # Passageiro ja cadastrado
            result["code"] = 1
            return Response(result, status = status.HTTP_200_OK)
        result["success"] = True
        return Response(result, status = status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        result = {}
        result["success"] = False
        try:
            queryPassageiro= Passageiro.objects.get(cpf = pk)
        except:
            # Motorista nao encontrado
            result["code"] = 1
            return Response(result, status = status.HTTP_200_OK)
        result["nome"] = queryPassageiro.nome
        result["date"] = queryPassageiro.data_nascimento
        result["sexo"] = queryPassageiro.sexo
        result["success"] = True
        return Response(result, status = status.HTTP_200_OK)


class motoristaView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    renderer_classes = (JSONRenderer,)

    def retrieve(self, request, pk=None):
        result = {}
        result["success"] = False
        try:
            queryMotorista = Motorista.objects.get(cpf = pk)
        except:
            # Motorista nao encontrado
            result["code"] = 1
            return Response(result, status = status.HTTP_200_OK)
        result["nome"] = queryMotorista.nome
        result["date"] = queryMotorista.data_nascimento
        result["modelo"] = queryMotorista.modelo
        result["status"] = queryMotorista.status
        result["sexo"] = queryMotorista.sexo
        result["success"] = True
        return Response(result, status = status.HTTP_200_OK)


    def create(self, request):
        result = {}
        result["success"] = False
        data = request.data
        # print str(datetime.strptime(data["date"], "%Y-%m-%d").date())
        date = datetime.strptime(data["date"], "%Y-%m-%d").date()
        cpf_treated = str(data["cpf"].replace(".","").replace("-",""))
        try:
            Motorista.objects.create(
            nome = str(data["nome"]),
            data_nascimento = date,
            cpf = cpf_treated,
            modelo = str(data["modelo"]),
            status = str(data["status"]),
            sexo = str(data["sexo"])
            )
        except Exception:
            # Motorista ja cadastrado
            result["code"] = 1
            return Response(result, status = status.HTTP_200_OK)
        result["success"] = True
        return Response(result, status = status.HTTP_200_OK)

class corridaView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    renderer_classes = (JSONRenderer,)

    def list(self, request):
        print 'entrou list'
        return Response({}, status = status.HTTP_200_OK)


    def create(self, request):
        result = {}
        result["success"] = False
        data = request.data
        # print str(datetime.strptime(data["date"], "%Y-%m-%d").date())
        valor = float(data.get('valor', 0))
        cpf_Passageiro_treated = str(data["cpfPassageiro"].replace(".","").replace("-",""))
        cpf_Motorista_treated = str(data["cpfMotorista"].replace(".","").replace("-",""))

        motoristaQuery = Motorista.objects.filter(cpf = cpf_Motorista_treated).values_list('id').first()
        passageiroQuery = Passageiro.objects.filter(cpf = cpf_Passageiro_treated).values_list('id').first()
        
        if passageiroQuery is None:
            result["code"] = 1

        if motoristaQuery is None:
            try:
                if result["code"] == 1:
                    result["code"] = 3
            except:
                result["code"] = 2

        if "code" in result:
            return Response(result, status = status.HTTP_200_OK)
        
        Corrida.objects.create(
        passageiro_id = passageiroQuery[0],
        motorista_id = motoristaQuery[0],
        valor = valor
        )

        result["success"] = True
        return Response(result, status = status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        result = {}
        result["success"] = False
        limit_offset = (int(pk)*5)
        corridaQuery = Corrida.objects.filter().order_by("-created_date")[limit_offset:limit_offset+5]
        print str(corridaQuery)
        result["corridas"] = []
        for item in corridaQuery:
            aux = {}
            aux['passageiro'] = item.passageiro.cpf
            aux['motorista'] = item.motorista.cpf
            aux['valor'] = item.valor
            result["corridas"].append(aux)
        result["success"] = True
        return Response(result, status = status.HTTP_200_OK)