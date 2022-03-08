#Créez un programme demandant à un utilisateur d'entrer sa date de fête et retournez-lui sa saison de naissance 
#s'il est né dans l'hémisphère Nord. (Vous pouvez assumer que les équinoxes et solstices ont lieu le 21 du mois.)

def saison_de_naissance():
    

jour = int(input("Quel est le jour de votre anniversaire:"))
mois = int(input("Quel est le mois de votre anniversaire:"))

saison = ["Automne", "Hiver", "Printemps", "Été"]

a, h, p, e = saison