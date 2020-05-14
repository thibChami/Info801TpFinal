import Afficheur


global  tup1
tup1 = ("test","test2",1,2,3) 
 

def main():
    print("Quel produit souhaitez vous?")
    product = input()
    print("Caractéristiques techniques?")
    technical = input()
    print("En combien de jours?")
    delay = input()
    print("Combien d'exemplaires?")
    quantity = input()
    print("Quel cout?")
    cost = input()
    tup1 = (product, technical, delay, quantity, cost)



    Afficheur.afficheur(tup1);

    print("Entrez le numéro de la solution qui vous convient:")
    solution = input()

    print ("vous avez choisi")
    
    
if __name__ == "__main__":
    main();
