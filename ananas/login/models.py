from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Campus(models.Model):
	nom=models.CharField(max_length=30)
	adresse=models.CharField(max_length=100)

	class Meta:
		verbose_name='Campus'
	def __str__(self):
		return self.nom

class Majeures(models.Model):
	nom=models.CharField(max_length=50)

	class Meta:
		verbose_name='Majeures'

	def __str__(self):
		return self.nom

class UserProfile(models.Model):
	user=models.OneToOneField(User,related_name='user',on_delete=models.CASCADE)
	avatar=models.ImageField(upload_to='avatar/')
	promo=models.IntegerField()
	naissance=models.CharField(max_length=10)
	phone=models.IntegerField()
	majeure=models.ForeignKey(Majeures,on_delete=models.CASCADE)
	campus=models.ForeignKey(Campus,on_delete=models.CASCADE)

	class Meta:
		verbose_name='User profile'

	def __str__(self):
		return self.user.nom

