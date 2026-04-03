pouce = 2.54
cm = 0.394
a = "pouce vers cm"
b = "cm vers pouce"





def demander_sens_conversion():
    while True:
        reponse = input(f"Vous souhaitez convertir de {a} ou de {b} ? ")
        if reponse == a or reponse == b:
            return reponse
        else:
            print(f"Vous devez répondre {a} ou {b}")




def demander_valeur_a_convertir():
    while True:
        try:
            valeur = float(input("Quelle valeur voulez vous convertir ? "))
            return valeur
        except:
            print("ERREUR : Vous devez entrer un nombre")





def convertir():
    sens = demander_sens_conversion()
    valeur = demander_valeur_a_convertir()
    if sens == a:
        resultat = valeur*pouce
        print(f"La conversion est {valeur} pouces = {resultat} cm" )
    else:
        resultat = valeur*cm
        print(f"{valeur} cm = {resultat} pouces")


convertir()
