# multi threading = used to perfom multiple tasks concurrently (multitasking)
#                   Good for I/O bound tasks like reding files or fetching data from APIs
#                   threading.Thread(target=my_function)

import threading
import time

def walk_dog(first , last):
    time.sleep(8)
    print(f"You finished walking {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("You would take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")

#walk_dog()     first executed
#take_out_trash()  after 1 executed fully then it starts 
#get_mail()         after 1 and 2 done fully then it starts

# all the three functions start executing simultaneously
chore1 = threading.Thread(target = walk_dog , args = {"Scooby","Doo"})
chore1.start()

chore2 = threading.Thread(target = take_out_trash)
chore2.start()

chore3 = threading.Thread(target = get_mail)
chore3.start()

#print("All chords are complete") if we do so print is executed first before all the chores

# print is executed at the end of all chores
chore1.join()
chore2.join()
chore3.join()
print("All chords are complete")   