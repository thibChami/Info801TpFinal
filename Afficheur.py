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
        while i < 3:
            with verrou:
                for lettre in self.phrase:
                    sys.stdout.write(lettre)
                    sys.stdout.flush()
                    # attente = 0.2
                    # attente += random.randint(1, 5) / 100
                    # time.sleep(attente)
            i += 1

# Création des threads
tup1 = ("pain", "frite", "avocat")
thread_1 = Afficheur(" Je vous propose " + tup1[random.randint(0, 2)] )
thread_2 = Afficheur(" second Thread ")

# Lancement des threads
thread_1.start()
thread_2.start()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()