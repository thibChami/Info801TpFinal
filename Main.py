import Afficheur
import threading
import time

espaceTuple = []

# !/usr/bin/python


exitFlag = 0


class myThread(threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        print_time(self.name, 5, self.counter)
        print("Exiting " + self.name)


def print_time(threadName, counter, delay):
    while len(espaceTuple) == 0:
        time.sleep(delay)
        print("%s: %s : %s" % (threadName, time.ctime(time.time()), "je susi en attente"))
    print(espaceTuple[0])
    # Afficheur.afficheur(espaceTuple[0]);
    time.sleep(5)

    if exitFlag:
        threadName.exit()


def main():
    # Create new threads
    thread1 = myThread(1, "maitre d'oeuvre", 1)
    # thread2 = myThread(2, "Thread-2", 2)

    # Start new Threads
    thread1.start()
    # thread2.start()

    print("Exiting Main Thread")

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

    espaceTuple.append(tup1)

    print("Entrez le numéro de la solution qui vous convient:")
    solution = input()

    print("vous avez choisi")


if __name__ == "__main__":
    main();