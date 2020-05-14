import random
import sys
from threading import Thread, RLock
import time
import Main
verrou = RLock()
global fabrication_list
class Afficheur(Thread):

    """Thread chargé simplement d'afficher un phrase dans la console."""

    def __init__(self, phrase):
        Thread.__init__(self)
        self.phrase = phrase

    def run(self):

        """Code à exécuter pendant l'exécution du thread."""

        with verrou:
            for lettre in self.phrase:
                sys.stdout.write(lettre)
                sys.stdout.flush()
                 # attente = 0.2
                 # attente += random.randint(1, 5) / 100
                 # time.sleep(attente)


# Création des threads
def afficheur(tup1):
    first_tuple =(tup1[0], tup1[1], (random.randint(1, int(tup1[2]))), (random.randint(1, int(tup1[3]))), (random.randint(1, int(tup1[4]))))
    second_tuple = (tup1[0], tup1[1], (random.randint(1, int(tup1[2]))), (random.randint(1, int(tup1[3]))), (random.randint(1, int(tup1[4]))))
    third_tuple =(tup1[0], tup1[1], (random.randint(1, int(tup1[2]))), (random.randint(1, int(tup1[3]))), (random.randint(1, int(tup1[4]))))
    fourth_tuple = (tup1[0], tup1[1], (random.randint(1, int(tup1[2]))), (random.randint(1, int(tup1[3]))), (random.randint(1, int(tup1[4]))))
    fifth_tuple = (tup1[0], tup1[1], (random.randint(1, int(tup1[2]))), (random.randint(1, int(tup1[3]))), (random.randint(1, int(tup1[4]))))
    fabrication_list = (first_tuple, second_tuple, third_tuple, fourth_tuple, fifth_tuple)

    thread_1 = Afficheur("1-" + " Je vous propose " + first_tuple[0] + ", les caracteristiques sont: " + first_tuple[1] + ", le produit vous sera délivré en " + str(first_tuple[2])
                         + " jours pour une quantité de " + str(first_tuple[3]) + " et le cout de production vous sera de " + str(first_tuple[4]) + " euros" + "\n")
    thread_2 = Afficheur("2-" + " Je vous propose " + second_tuple[0] + ", les caracteristiques sont: " + second_tuple[1] + ", le produit vous sera délivré en " + str(second_tuple[2])
                         + " jours pour une quantité de " + str(second_tuple[3]) + " et le cout de production vous sera de " + str(second_tuple[4]) + " euros" + "\n")
    thread_3 = Afficheur("3-" + " Je vous propose " + third_tuple[0] + ", les caracteristiques sont: " + third_tuple[1] + ", le produit vous sera délivré en " + str(third_tuple[2])
                         + " jours pour une quantité de " + str(third_tuple[3]) + " et le cout de production vous sera de " + str(third_tuple[4]) + " euros" + "\n")
    thread_4 = Afficheur("4-" + " Je vous propose " + fourth_tuple[0] + ", les caracteristiques sont: " + fourth_tuple[1] + ", le produit vous sera délivré en " + str(fourth_tuple[2])
                         + " jours pour une quantité de " + str(fourth_tuple[3]) + " et le cout de production vous sera de " + str(fourth_tuple[4]) + " euros" + "\n")
    thread_5 = Afficheur("5-" + " Je vous propose " + fifth_tuple[0] + ", les caracteristiques sont: " + fifth_tuple[1] + ", le produit vous sera délivré en " + str(random.randint(1, int(fifth_tuple[2])))
                         + " jours pour une quantité de " + str(fifth_tuple[3]) + " et le cout de production vous sera de " + str(fifth_tuple[4]) + " euros" + "\n")

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