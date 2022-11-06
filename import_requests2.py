import requests 
from bs4 import BeautifulSoup
import csv

url = "https://www.gov.uk/search/news-and-communications"
reponse = requests.get(url)
#print(reponse)
page = reponse.content
#print(page)
soup = BeautifulSoup(page, "html.parser")
#print(soup.title)
print(soup.title.string)
class_name = "gem-c-document-list__item-title"
titres_bs = soup.find_all("a", class_=class_name)
titres = []
for titre in titres_bs:
    titres.append(titre.string)
#print(titres)
descriptions_bs = soup.find_all("p", class_="gem-c-document-list__item-description")
descriptions = []
for desc in descriptions_bs:
    descriptions.append(desc.string)
#print(descriptions)

# Créer une liste pour les en-têtes
en_tete = ["titre", "description"]

# Créer un nouveau fichier pour écrire dans le fichier appelé « data.csv »
with open('data.csv', 'w') as fichier_csv:
   # Créer un objet writer (écriture) avec ce fichier
   writer = csv.writer(fichier_csv, delimiter=',')
   writer.writerow(en_tete)
   # Parcourir les titres et descriptions - zip permet d'itérer sur deux listes ou plus à la fois
   for titre, description in zip(titres, descriptions):
      # Créer une nouvelle ligne avec le titre et la description à ce moment de la boucle
      ligne = [titre, description]
      writer.writerow(ligne)
