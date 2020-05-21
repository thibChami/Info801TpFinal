import Afficheur
import threading
import time


stop =0
espaceTupleClient = []
espaceTupleMO = []
espaceTupleCond = []
espaceTupleT = []
#!/usr/bin/python



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
        print ("Exiting " + self.name)
     
            
            
def maitre_oeuvre(threadName, counter, delay):
    global espaceTupleMO
    while  not stop :
        if len(espaceTupleMO) != 0 :
            time.sleep(delay)
                #print ("%s: %s : %s" % (threadName, time.ctime(time.time()) , "je susi en attente"))
            print(espaceTupleMO[0])
            for x in Afficheur.afficheur(espaceTupleMO[0]):
                espaceTupleClient.append(x)
            print(espaceTupleMO)
            espaceTupleMO=[]   
            
            time.sleep(5)
    
    if exitFlag:
         threadName.exit()

def conditionnement(threadName, counter, delay):
    global espaceTupleCond
    print("cond")
    while  not stop :
        if len(espaceTupleCond) != 0 :
            time.sleep(delay)
                #print ("%s: %s : %s" % (threadName, time.ctime(time.time()) , "je susi en attente"))
            print(espaceTupleCond[0])
            for x in Afficheur.afficheur2(espaceTupleCond[0]):
                espaceTupleClient.append(x)
            print(espaceTupleCond)
            espaceTupleCond=[]   

            time.sleep(5)
    if exitFlag:
         threadName.exit()


def transport(threadName, counter, delay):
    global espaceTupleT
    print("t");
    
    while  not stop :
        if len(espaceTupleT) != 0 :
            time.sleep(delay)
                #print ("%s: %s : %s" % (threadName, time.ctime(time.time()) , "je susi en attente"))
            print(espaceTupleT[0])
            for x in Afficheur.afficheur3(espaceTupleT[0]):
                espaceTupleClient.append(x)
            print(espaceTupleT)
            espaceTupleT=[]   

            time.sleep(5)


    if exitFlag:
         threadName.exit()         

def main():
    global espaceTupleMO
    global espaceTupleClient
    global espaceTupleCond
    global espaceTupleT


    # Create new threads
    thread1 = myThread(1, "maitre d'oeuvre", 2)
    thread2 = myThread(2, "conditionnement", 2)
    thread3 = myThread(3, "transport", 2)

    # Start new Threads
    thread1.start()
    thread2.start()
    thread3.start()



    
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
        
        
        print("Entrez le numéro de la solution qui vous convient:")
        solution = input()
        print(solution)
        if solution == "0" :
            print  ("vous avez rien choisi")

        else:
            res = espaceTupleClient[int(solution)-1]
            print  ("vous avez choisi :" , res)
            choose = 1
        espaceTupleMO=[]
        espaceTupleClient=[]

    

    choose =0
    while not choose :
        espaceTupleCond.append((50,"test"))
        time.sleep(5)

        while len(espaceTupleClient) == 0 :
            time.sleep(5)
        
        
        print("Entrez le numéro de la solution qui vous convient:")
        solution = input()
        print(solution)
        if solution == "0" :
            print  ("vous avez rien choisi")

        else:
            res = espaceTupleClient[int(solution)-1]
            print  ("vous avez choisi :" , res)
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
        print(solution)
        if solution == "0" :
            print  ("vous avez rien choisi")

        else:
            res = espaceTupleClient[int(solution)-1]
            print  ("vous avez choisi :" , res)
            choose = 1
        espaceTupleClient=[]
        espaceTupleT=[]
        
        
    print("stop")  
    global stop
    stop =1
    
   
if __name__ == "__main__":
    main();
