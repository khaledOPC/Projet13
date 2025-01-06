from webapp.models import Category
from django.core.management.base import BaseCommand

'''
Ajout des categories à partir du fichier populate_category et evite les doublons.
'''
def add_category(elements): 
	
	for element in elements:
		element, created = Category.objects.get_or_create(name=element)
		if created:
			print(f"la categorie {element} à été créée")
		else:
			print(f"la categorie {element} existe déjà")

'''
Définition de la class Command pour utiliser le script en tant que commande via manage.py.
'''
class Command(BaseCommand):
	help = "Importe les produits à partir d'Open Food Facts"

	def handle(self, *args, **kwargs):
		create_categories = [
		"Sport",
		"Culture",
		"En famille",
		"Loisir",
		"Voyage",
		"Technologie",
		"Santé",
		"Éducation",
		"Musique",
		"Art",
		"Cuisine",
		"Mode",
		"Histoire",
		"Nature",
		"Littérature",
		"Science",
		"Cinéma",
		"Photographie",
		"Jeux vidéo",
		"Théâtre"
		]
		category_data = add_category(create_categories)