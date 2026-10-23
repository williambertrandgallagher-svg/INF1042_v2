"""
Exemple 6 — Choix aléatoire et condition

random.choice() choisit un élément dans une collection.
"""

import random

options = ["Pierre", "Papier", "Ciseaux"]
choix = random.choice(options)

#choix_joueur = int(input("Choisi Pierre, Papier ou Ciseaux : "))
#if choix_joueur == "Pierre" or "Papier" or "Ciseaux":
#    print("Erreur, mauvais choix")
#else:
#    print("Choix de l'ordinateur :", choix)

#    if choix == "Pierre" and choix_joueur == "Pierre":
#        print("Égalité! Pas de gagnant(e)")
#    elif choix == "Papier" and choix_joueur == "Pierre":
#        print("Félicitations! Vous avez gagnez")
#    elif choix == "Ciseaux" and choix_joueur == "Pierre":
#        print("Vous avez perdu!")
#    elif choix == "Pierre" and choix_joueur == "Papier":
#        print("Félicitations! Vous avez gagnez")
#    elif choix == "Papier" and choix_joueur == "Papier":
#        print("Égalité! Pas de gagnant(e)")
#    elif choix == "Ciseaux" and choix_joueur == "Papier":
#        print("Vous avez perdu!")
#    elif choix == "Pierre" and choix_joueur == "Ciseaux":
#        print("Vous avez perdu!")
#    elif choix == "Papier" and choix_joueur == "Ciseaux":
#        print("Félicitations! Vous avez gagnez")
#    elif choix == "Ciseaux" and choix_joueur == "Ciseaux":
#        print("Égalité! Pas de gagnant(e)")