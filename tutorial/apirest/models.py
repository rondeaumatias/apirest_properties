from django.db import models

class Property (models.Model):
	title = models.CharField(verbose_name="title", max_length=40)
	address = models.CharField(verbose_name="address", max_length=100)
	description= models.TextField(verbose_name="description", max_length=1000)
	person_owner = models.ForeignKey("Person", blank=True, null=True, on_delete=models.CASCADE, related_name="properties")
	lat = models.CharField(verbose_name="latitude", max_length=20)
	length = models.CharField(verbose_name="length", max_length=20)
	price = models.IntegerField(verbose_name="price")
	PROP_TYPE = (
		('d','departament'),
		('h', 'house'),
		('l','local'),
	)
	prop_type= models.CharField(max_length=1, choices=PROP_TYPE,blank=True, help_text='Tipo de Local')

	def __str__(self):
		return '%s, %s' % (self.id, self.title)

	#def get_all (self):
#		return ','.join([ owner.name for owner in self.owner.all()[:5] ])




class Person (models.Model):
	dni = models.CharField(verbose_name="document_identity", max_length=8)
	name = models.CharField(verbose_name="name", max_length=30)
	lastname = models.CharField(verbose_name="lastname", max_length=30)
	celphone_contact = models.CharField(verbose_name="number_phone", max_length=50)
	address = models.CharField(verbose_name="personal_address", max_length=100)

	def __str__(self):
		return '%s, %s' % (self.name, self.lastname)

#	def get_absolute_url(self):
#		return reverse('person-detail', args=[str(self.id)])

#	class Meta: 
#		ordering = ['lastname']



