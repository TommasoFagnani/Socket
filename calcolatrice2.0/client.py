import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
    sock_service.connect((SERVER_IP,SERVER_PORT))
    while True:
        primoNumero=float(input("inserire numero "))
        operazione=input("inserire l'operatore (+,-,*,/,%) ")
        secondoNumero=float(input("inserire il secondo numero "))
        message={
            'primoNumero':primoNumero,
            'operazione':operazione,
            'secondoNumero':secondoNumero
            }
        message=json.dumps(message) 
        sock_service.sendall(message.encode("UTF-8"))
        data=sock_service.recv(BUFFER_SIZE)
        print("risultato: ",data.decode())

        risp=input("se non vuoi fare altre operazioni digita 'n'==no ")
        if(risp=='n'):
            break
