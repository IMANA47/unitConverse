# =========================================================
# Fichier      : app.py
# Projet       : Mini conversion d'unités en ligne de commande
# Description  : Ce programme permet de convertir des pouces (inch) en centimètres (cm), et vice-versa.
# Auteur       : Francois Nsengimana
# Créé le      : 03/04/2026
# Version      : 1.0.0
# Python       : 3.14.0
# =========================================================




# Les unite de mesure
unite_pouce = 2.54   # cm
unite_centimettre = 0.394 #pouces

#1 - Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces"

question_conversion = int(input("souhaite convertir de pouces vers cm ou cm vers pouces? \n Repondez 1 pour pouce vers cm et 2 pour cm vers pouces :"))


# 2 - Demander à l'utilisateur de rentrer la valeur à convertir (en réaffichant l’unité demandée)
if question_conversion == 1:
    response_cm = float(input("Entre la valeurs a convertir pour pouce vers cm : "))
    conversion_en_cm = response_cm * unite_pouce
    conversion_en_cm = round(conversion_en_cm, 2)

    print(f"Votre valeurs {response_cm} en pouce est {conversion_en_cm} cm")

elif question_conversion == 2:
    response_pouce = float(input("Entre la valeurs a convertir pour cm vers pouce : "))
    conversion_en_pouce = response_pouce * unite_centimettre
    conversion_en_pouce = round(conversion_en_pouce, 2)
    print(f"Votre valeurs {response_pouce} en pouce est {conversion_en_pouce} pouces")



