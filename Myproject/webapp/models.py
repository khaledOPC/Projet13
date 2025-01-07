from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model
# Create your models here.


'''
class pour gérer les category d'activité, Sport, culture, loisir..
'''
class Category(models.Model):
	name = models.CharField(max_length=200, unique=True)
	image = models.ImageField(upload_to='image_category/', blank=True, null=True)

	def __str__(self):
		return self.name

'''
class pour gérer les activités
'''
class Activity(models.Model):
	name = models.CharField(max_length=100)
	lieu = models.CharField(max_length=200)
	max_participants = models.PositiveIntegerField(default=10)
	date = models.DateField()
	image = models.ImageField(upload_to ='image_activity/', blank=True, null=True) 
	category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)

	def __str__(self):
		return self.name

	'''
	Méthode pour comptabiliser le nombre de réservation?
	'''
	def check_reservations(self):
		check_reservation = Reservation.objects.filter(activity=self).count()
		return check_reservation


	'''
	Fonction pour vérifier si la reservation est possible.
	'''
	def can_reserve(self):
		return self.check_reservations() < self.max_participants


'''
class pour gérer les réservations.
'''
class Reservation(models.Model):
	date = models.DateField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	activity = models.ForeignKey(Activity, on_delete=models.CASCADE)


	def __str__(self):
		return f"Réservation de {self.user.username} pour l'activité {self.activity.name} le {self.date}"

	'''
	Fonction pour s'assurer que la réservation est possible et assurer la logique de la class.
	'''
	def save(self, *args, **kwargs):
		if not self.activity.can_reserve():
			raise ValueError("Le nombre de Réservation maximum est déja atteint")
		if self.date != self.activity.date:
			raise ValueError("La date de Reservation ne correspond pas à celle de l'activité choisis")
		super().save(*args, **kwargs)
