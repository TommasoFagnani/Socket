import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((SERVER_IP,SERVER_PORT)) 
    print('Comandi disponibili: \n #list : per vedere i voti inseriti \n #get /nomestudente : per richiedere i voti di uno studente \n #set /nomestudente : per inserire uno studente \n #put /nomestudente/materia/voto/ore : per aggiungere i voti della materia allo studente \n #close : per chiudere la connessione')

    while True:
            
        comando = (input("Inserisci comando: "))
        if (comando != "#list" and comando != "#close"):
            parametri = (input("Inserisci studente (preceduto da /): "))
        elif(comando == "#close"):
            parametri = " "
            break
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
        
        
        