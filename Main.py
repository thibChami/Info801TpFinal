import Afficheur
import threading
import time


stop =0
espaceTupleClient = []
espaceTupleMO = []
espaceTupleCond = []
espaceTupleT = []
espaceTupleDetail = []
#!/usr/bin/python
rest =[]


exitFlag = 0

class myThread (threading.Thread):
   
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   
   def run(self):
        print ("Starting " + self.name)
        if self.name == "maitre d'oeuvre":
            maitre_oeuvre(self.name, 5, self.counter)
        if self.name == "conditionnement":
            conditionnement(self.name, 5, self.counter)
        if self.name == "transport":
            transport(self.name, 5, self.counter) 
        if self.name == "detaillant":
            detaillant(self.name, 5, self.counter) 
            
            
            
        print ("Exiting " + self.name)
     
            
            
def maitre_oeuvre(threadName, counter, delay):
    global espaceTupleMO
    while  not stop :
        if len(espaceTupleMO) != 0 :
            time.sleep(delay)
                #print ("%s: %s : %s" % (threadName, time.ctime(time.time()) , "je susi en attente"))

            for x in Afficheur.afficheur(espaceTupleMO[0]):
                espaceTupleClient.append(x)
            espaceTupleMO=[]   
            
            time.sleep(5)
    
    if exitFlag:
         threadName.exit()

def conditionnement(threadName, counter, delay):
    global espaceTupleCond
    while  not stop :
        if len(espaceTupleCond) != 0 :
            time.sleep(delay)
                #print ("%s: %s : %s" % (threadName, time.ctime(time.time()) , "je susi en attente"))
            for x in Afficheur.afficheur2(espaceTupleCond[0]):
                espaceTupleClient.append(x)
            espaceTupleCond=[]   

            time.sleep(5)
    if exitFlag:
         threadName.exit()


def transport(threadName, counter, delay):
    global espaceTupleT

    
    while  not stop :
        if len(espaceTupleT) != 0 :
            time.sleep(delay)
                #print ("%s: %s : %s" % (threadName, time.ctime(time.time()) , "je susi en attente"))
            for x in Afficheur.afficheur3(espaceTupleT[0]):
                espaceTupleClient.append(x)
            espaceTupleT=[]   

            time.sleep(5)


    if exitFlag:
         threadName.exit()   
         
def detaillant(threadName, counter, delay):
    global espaceTupleDetail

    
    while  not stop :
        if len(espaceTupleDetail) != 0 :
            time.sleep(delay)
                #print ("%s: %s : %s" % (threadName, time.ctime(time.time()) , "je susi en attente"))
            for x in Afficheur.afficheur4(espaceTupleDetail[0]):
                espaceTupleClient.append(x)
            espaceTupleDetail=[]   

            time.sleep(5)


    if exitFlag:
         threadName.exit()      
def main():
    global espaceTupleMO
    global espaceTupleClient
    global espaceTupleCond
    global espaceTupleT
    global rest
    global espaceTupleDetail
    # Create new threads
    thread1 = myThread(1, "maitre d'oeuvre", 2)
    thread2 = myThread(2, "conditionnement", 2)
    thread3 = myThread(3, "transport", 2)
    thread4 = myThread(4, "detaillant", 2)

    # Start new Threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()



    
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
    choose = 0

    while not choose :
        espaceTupleMO.append(tup1)
        time.sleep(5)

        while len(espaceTupleClient) == 0 :
                time.sleep(5)
        
        
        print(" Entrez le numéro de la solution qui vous convient: ")
        solution = input()
        print(solution)
        if solution == "0" :
            print  ("vous n'avez rien choisi ")

        else:
            rest.append(espaceTupleClient[int(solution)-1])
            res = rest[0]
            print  ("vous avez choisi :" , str(res[0]) + ", les caracteristiques sont: " + res[1] + ", le produit vous sera délivré en " + str(res[2])
                         + " jours pour une quantité de " + str(res[3]) + " et le cout de production vous sera de " + str(res[4]) + " euros" + "\n")
            choose = 1
        espaceTupleMO=[]
        espaceTupleClient=[]

    

    choose =0
    while not choose :
        espaceTupleCond.append((50,"test"))
        time.sleep(5)

        while len(espaceTupleClient) == 0 :
            time.sleep(5)
        
        
        print("Entrez le numéro de la solution qui vous convient : ")
        solution = input()
        if solution == "0" :
            print  ("vous avez rien choisi")

        else:
           rest.append(espaceTupleClient[int(solution)-1])
           res = rest[1]
           print  ("vous avez choisi : " ,  "le matériau " + res[1] + " cela vous coutera " + str(res[0]) + " €" )
           choose = 1
        espaceTupleClient=[]
        espaceTupleCond=[]
   
    
    choose =0
    
    
    while not choose :
        espaceTupleT.append((90,"test"))
        time.sleep(5)

        while len(espaceTupleClient) == 0 :
            time.sleep(5)
        
        
        print("Entrez le numéro de la solution qui vous convient:")
        solution = input()
        if solution == "0" :
            print  ("vous avez rien choisi")

        else:
            rest.append(espaceTupleClient[int(solution)-1])
            res = rest[2]
            print  ("vous avez choisi :" ,    " La société " + str(res[1]) + " et  le transport durera   " + str(res[0]) +     " min " + "le cout sera de 50 € \n")

            choose = 1
        espaceTupleClient=[]
        espaceTupleT=[]
      


    choose =0
    
    cout = rest[0][4] +rest[1][0] +50
    while not choose :
        espaceTupleDetail.append((cout  ,"test"))
        time.sleep(5)

        while len(espaceTupleClient) == 0 :
            time.sleep(5)
        
        
        print("Entrez le numéro de la solution qui vous convient:")
        solution = input()
        if solution == "0" :
            print  ("vous avez rien choisi")

        else:
            rest.append(espaceTupleClient[int(solution)-1])
            res = rest[3]
            print  ("vous avez choisi :" ,    " Le revendeur  " + str(res[1]) + " il revendra le produit  pour  " + str(res[0]) +    " €   vous ferez "+ str(res[0] - cout) + "€ de bénéfice " +" \n")

            choose = 1
        espaceTupleClient=[]
        espaceTupleDetail=[]

    
        
    print  ("vous avez fait un totale de "+ str(res[0] - cout    * rest[0][3] )   + "€ de bénéfice au totale  " +" \n")
     
    print("stop")  
    global stop
    stop =1
    
   
if __name__ == "__main__":
    main();
