import random
import sys
from threading import Thread, RLock
import time
import Main
verrou = RLock()

class Afficheur(Thread):

    """Thread chargé simplement d'afficher un phrase dans la console."""

    def __init__(self, phrase):
        Thread.__init__(self)
        self.phrase = phrase

    def run(self):

        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        while i < 1:
            with verrou:
                for lettre in self.phrase:
                    sys.stdout.write(lettre)
                    sys.stdout.flush()
                    # attente = 0.2
                    # attente += random.randint(1, 5) / 100
                    # time.sleep(attente)
            i += 1

# Création des threads

thread_1 = Afficheur("1-" + " Je vous propose " + Main.tup1[0] + ", les caracteristiques sont: " + Main.tup1[1] + ", le produit vous sera délivré en " + Main.tup1[2]
                     + " jours pour une quantité de " + Main.tup1[3] + " et le cout de production vous sera de " + str(random.randint(1, 50)) + " euros" + "\n")
thread_2 = Afficheur("2-" + " Je vous propose " + Main.tup1[0] + ", les caracteristiques sont: " + Main.tup1[1] + ", le produit vous sera délivré en " + Main.tup1[2]
                     + " jours pour une quantité de " + Main.tup1[3] + " et le cout de production vous sera de " + Main.tup1[4] + " euros" + "\n")
thread_3 = Afficheur("3-" + " Je vous propose " + Main.tup1[0] + ", les caracteristiques sont: " + Main.tup1[1] + ", le produit vous sera délivré en " + Main.tup1[2]
                     + " jours pour une quantité de " + Main.tup1[3] + " et le cout de production vous sera de " + Main.tup1[4] + " euros" + "\n")
thread_4 = Afficheur("4-" + " Je vous propose " + Main.tup1[0] + ", les caracteristiques sont: " + Main.tup1[1] + ", le produit vous sera délivré en " + Main.tup1[2]
                     + " jours pour une quantité de " + Main.tup1[3] + " et le cout de production vous sera de " + Main.tup1[4] + " euros" + "\n")
thread_5 = Afficheur("5-" + " Je vous propose " + Main.tup1[0] + ", les caracteristiques sont: " + Main.tup1[1] + ", le produit vous sera délivré en " + Main.tup1[2]
                     + " jours pour une quantité de " + Main.tup1[3] + " et le cout de production vous sera de " + Main.tup1[4] + " euros" + "\n")

# Lancement des threads
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_5.start()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
thread_5.join()