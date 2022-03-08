#Créez un programme demandant à un utilisateur d'entrer sa date de fête et retournez-lui sa saison de naissance 
#s'il est né dans l'hémisphère Nord. (Vous pouvez assumer que les équinoxes et solstices ont lieu le 21 du mois.)
#primtemps hémisphère nord 21 mars 21 juin
#été hémisphère nord 22 juin 22 sept
#automne hémisphère 22 sept 21 dec
#hiver hémisphère nord 22 dec 20 mars

def saison_de_naissance():
    
    if 2 < mois < 7:
        print("Vous ête née au printemps!")
    elif 5 < mois < 9:
        print("Vous êtes née en été!")
    elif 10 < mois <= 11:
        print("Vous êtes née en automne!")
    else:
        print("Vous êtes née en hiver!")
    return

    

#jour = int(input("Quel est le jour de votre anniversaire:"))
mois = int(input("Quel est le mois de votre anniversaire en entier:"))
#hemisphere = str(input("Êtes-vous dans l'hémisphère nord ou sud:"))



saison_de_naissance()