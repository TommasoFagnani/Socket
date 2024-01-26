import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024
#com

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((SERVER_IP,SERVER_PORT))
    while True:
        comando = (input("Inserisci comando: "))
        if (comando != "#list"):
            parametri = (input("Inserisci studente: "))
        else:
            parametri = " "
 
        
        istruzioni = {
            "comando":comando,
            "parametri":parametri,
        }
        
        istruzioni=json.dumps(istruzioni) 
        sock.sendall(istruzioni.encode("UTF-8"))
        dati=sock.recv(BUFFER_SIZE)
        print(dati.decode())

#chiusura socket
#sock.close()