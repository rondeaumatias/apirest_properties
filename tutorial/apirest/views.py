from django.shortcuts import render
from .models import Property, Person

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .serializers import PersonSerializer, PropertySerializer

#from django.views.decorators.csrf import csrf_exempt

class PersonList(generics.ListCreateAPIView):
	queryset = Person.objects.all()
	serializer_class= PersonSerializer


class PersonDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset= Person.objects.all()
	serializer_class= PersonSerializer	


class PropertyList(generics.ListCreateAPIView):
	queryset= Property.objects.all()
	serializer_class= PropertySerializer

class PropertyDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset= Property.objects.all()
	serializer_class=PropertySerializer