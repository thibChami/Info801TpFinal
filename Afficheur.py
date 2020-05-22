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
    
    
    return     first_tuple,second_tuple, third_tuple,fourth_tuple ,fifth_tuple
    
    
    
    
def afficheur2(tup1):
    prix = tup1[0]
    liste_mat = ("verre","Aluminium","Plastiques","PVC","metal")
    first_tuple =((random.randint(1, prix)), liste_mat[(random.randint(0,len(liste_mat)-1))])
    second_tuple = ((random.randint(1, prix)), liste_mat[(random.randint(0,len(liste_mat)-1))])
    third_tuple =((random.randint(1, prix)), liste_mat[(random.randint(0,len(liste_mat)))-1])
    fourth_tuple = ((random.randint(1, prix)), liste_mat[(random.randint(0,len(liste_mat)))-1])
    fifth_tuple = ((random.randint(1, prix)), liste_mat[(random.randint(0,len(liste_mat)))-1])

    thread_1 = Afficheur("1-" + " Je vous propose " + str(first_tuple[0]) + "€ pour le prix et pour le matériau  " + first_tuple[1] +    "\n")
    thread_2 = Afficheur("2-" + " Je vous propose " +  str(second_tuple[0]) + "€ pour le prix et pour le matériau  " + second_tuple[1] +    "\n")
    thread_3 = Afficheur("3-" + " Je vous propose " +  str(third_tuple[0]) + "€ pour le prix et pour le matériau  " + third_tuple[1] +    "\n")
    thread_4 = Afficheur("4-" + " Je vous propose " +  str(fourth_tuple[0])+ "€ pour le prix et pour le matériau  " + fourth_tuple[1] +    "\n")
    thread_5 = Afficheur("5-" + " Je vous propose " +  str(fifth_tuple[0]) + "€ pour le prix et pour le matériau  " + fifth_tuple[1] +    "\n")
   
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
    
    return     first_tuple,second_tuple, third_tuple,fourth_tuple ,fifth_tuple


def afficheur3(tup1):
    temps = tup1[0]
    liste_T = ("Ensemble Transport","Transport Éclaireur","Virtuel Transport","Celtique Transport", "Hometown Transport","Vivant Transport","Agora Transport","Trinity Transport","Quark Transport","Transport Metric","Mermaid Transport","Émergent Transport","Transport Rail","Transport Safari","Transport Champion","Transport Vétéran")


    first_tuple =((random.randint(25, temps)), liste_T[(random.randint(0,len(liste_T)-1))])
    second_tuple = ((random.randint(25, temps)), liste_T[(random.randint(0,len(liste_T)-1))])
    third_tuple =((random.randint(25, temps)), liste_T[(random.randint(0,len(liste_T)))-1])
    fourth_tuple = ((random.randint(25, temps)), liste_T[(random.randint(0,len(liste_T)))-1])
    fifth_tuple = ((random.randint(25, temps)), liste_T[(random.randint(0,len(liste_T)))-1])

    thread_1 = Afficheur("1-" + " La société " + str(first_tuple[1]) + " propose de faire le transport en   " + str(first_tuple[0]) +    " min\n")
    thread_2 = Afficheur("2-" + " La société " + str(second_tuple[1]) + " propose de faire le transport en   " + str(second_tuple[0]) +    " min\n")
    thread_3 = Afficheur("3-" + " La société " + str(third_tuple[1]) + " propose de faire le transport en   " + str(third_tuple[0]) +    " min\n")
    thread_4 = Afficheur("4-" + " La société " + str(fourth_tuple[1]) + " propose de faire le transport en   " + str(fourth_tuple[0]) +    " min\n")
    thread_5 = Afficheur("5-"+ " La société " + str(fifth_tuple[1]) + " propose de faire le transport en   " + str(fifth_tuple[0]) +    " min\n")
   
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
    
    return     first_tuple,second_tuple, third_tuple,fourth_tuple ,fifth_tuple


def afficheur4(tup1):
    prix = tup1[0]
    liste_T = (" ESSO SOCIETE ANONYME FRANCAISE" , "AUCHAN HYPERMARCHE	","DISTRIBUTION CASINO FRANCE	","LEROY MERLIN FRANCE	","CORA" ,"DECATHLON FRANCE"," MEUBLES IKEA FRANCE","THEVENIN DUCROT DISTRIBUTION"," BRICO DEPOT"	,"CDISCOUNT	","CONFORAMA FRANCE"	,"VENTE PRIVEE.COM", "MAGASINS GALERIES LAFAYETTE	","PRINTEMPS" , "SUPERMARCHES MATCH	","ELECTRO DEPOT FRANCE" "PRIMARK FRANCE SAS" , "VETIR","DARTY GRAND EST" , "SHOWROOMPRIVE.COM	")

    first_tuple =((random.randint( prix,prix*3)), liste_T[(random.randint(0,len(liste_T)-1))])
    second_tuple = ((random.randint(prix,prix*3)), liste_T[(random.randint(0,len(liste_T)-1))])
    third_tuple =((random.randint(prix,prix*3)), liste_T[(random.randint(0,len(liste_T)))-1])
    fourth_tuple = ((random.randint(prix,prix*3)), liste_T[(random.randint(0,len(liste_T)))-1])
    fifth_tuple = ((random.randint(prix,prix*3)), liste_T[(random.randint(0,len(liste_T)))-1])

    thread_1 = Afficheur("1-" + " Le detaillant "+ str(first_tuple[1]) + " propose de revendre le produit   " + str(first_tuple[0]) +    " €\n")
    thread_2 = Afficheur("2-" + " Le detaillant " + str(second_tuple[1]) + " propose de revendre le produit  " + str(second_tuple[0]) +    " €\n")
    thread_3 = Afficheur("3-" + " Le detaillant  " + str(third_tuple[1]) + " propose de revendre le produit   " + str(third_tuple[0]) +    " €\n")
    thread_4 = Afficheur("4-" + "Le detaillant  " + str(fourth_tuple[1]) + " propose de revendre le produit   " + str(fourth_tuple[0]) +    " €\n")
    thread_5 = Afficheur("5-"+ " Le detaillant  " + str(fifth_tuple[1]) + " propose de revendre le produit  " + str(fifth_tuple[0]) +    " €\n")
   
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
    
    return     first_tuple,second_tuple, third_tuple,fourth_tuple ,fifth_tuple