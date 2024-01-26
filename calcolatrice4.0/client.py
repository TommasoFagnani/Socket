import socket
import sys
import random
import os
import time
import threading
import multiprocessing
import json

SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 22224
NUM_WORKERS = 15
BUFFER_SIZE = 2048

def genera_richieste(SERVER_ADDRESS,SERVER_PORT):
    try:
        start_time_thread=time.time()
        sock=socket.socket()
        sock.connect((SERVER_ADDRESS,SERVER_PORT))
    except:
        print(f"{threading.current_thread().name} errore")

    segni=["*","-","+","/","%"]
    primoNumero=random.randint(1,100)
    ind=random.randrange(0,4)
    operazione=segni[ind]
    
    secondoNumero=random.randint(1,100)

    messaggio = {
        "primoNumero":primoNumero,
        "operazione":operazione,
        "secondoNumero":secondoNumero
    }
    
    print(f"{threading.current_thread().name}, messaggio:" ,messaggio)

    messaggio = json.dumps(messaggio)
    sock.sendall(messaggio.encode("UTF-8"))
    data = sock.recv(BUFFER_SIZE)
    print("Risultato:", data.decode())

    end_time_thread = time.time()
    print(f"{threading.current_thread().name} excution time =", end_time_thread - start_time_thread)

if __name__ == '__main__':
   # Run tasks using threads
   start_time = time.time()
   threads= [threading.Thread(target=genera_richieste, args=(SERVER_ADDRESS, SERVER_PORT,)) for _ in range (NUM_WORKERS)]
   [thread.start() for thread in threads]
   [thread.join() for thread in threads]
   end_time = time.time()

   print("Total threads time=", end_time - start_time)
