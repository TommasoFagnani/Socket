import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 22007
BUFFER_SIZE = 1024


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP,SERVER_PORT))
print("Connesso a: ", (SERVER_IP,SERVER_PORT))
while True:
    primoNumero = float(input("Inserisci il primo numero: "))
    operazione = input("Inserisci l'operazione (+, -, *, /, %): ")
    secondoNumero = float(input("Inserisci il secondo numero: "))
    messaggio = {
        "primoNumero":primoNumero,
        "operazione":operazione,
        "secondoNumero":secondoNumero
    }
    messaggio = json.dumps(messaggio)
    sock.sendall(messaggio.encode("UTF-8"))
    data = sock.recv(BUFFER_SIZE)
    print("Risultato:", data.decode())
    risp=input("se non vuoi fare altre operazioni digita 'n'==no ")
    if(risp=='n'):
        print("chiusura della connessione col server")
        break
        
        
    