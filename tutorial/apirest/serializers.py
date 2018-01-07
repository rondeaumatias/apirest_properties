from .models import Person, Property
#from django.contrib.auth.models import User
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields= ('name','lastname','celphone_contact','address')
		
class PropertySerializer(serializers.ModelSerializer):
	class Meta:
		model= Property
		fields=('title','address','description','person_owner','lat','length','price','prop_type')
