import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

#Creazione del socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((SERVER_IP,SERVER_PORT))
    sock.listen()
    print(f"Server in ascolto su {SERVER_IP}:{SERVER_PORT}...")

    while True:
        sock, address_client = sock.accept()
        
        with sock as sock_client:
            while True:
                istruzioni = sock.recv(BUFFER_SIZE).decode()
                if not istruzioni:
                    break
                
                istruzioni = json.loads(istruzioni)
                print(istruzioni)
                comando = (istruzioni["comando"]).split("#")[1]
                parametri = istruzioni["parametri"]
            
                print(comando)

                diz={'Antonio Barbera': [   ['Matematica', 8, 1],
                                    ['Italiano', 6, 1],
                                    ['Inglese', 9.5, 0],
                                    ['Storia', 8, 2],
                                    ['Geografia', 8, 1]],
                'Giuseppe Gullo': [   ['Matematica', 9, 0],
                                    ['Italiano', 7, 3],
                                    ['Inglese', 7.5, 4],
                                    ['Storia', 7.5, 4],
                                    ['Geografia', 5, 7]],
                'Nicola Spina': [   ['Matematica', 7.5, 2],
                                    ['Italiano', 6, 2],
                                    ['Inglese', 4, 3],
                                    ['Storia', 8.5, 2],
                                    ['Geografia', 8, 2]]}
                
                if comando == "list":
                    risp = "OK"
                    risultato = diz

                elif comando == "get":
                    studente = parametri
                    if studente in diz:
                        risp = "OK"
                        risultato = diz[studente]
                    else:
                        risp = "KO",
                        risultato = "Studente non presente"

                elif comando == "set":
                    studente = parametri
                    if studente not in diz:
                        diz[studente] = {}
                        risp = "OK"
                        risultato = "Studente inserito"
                    else:
                        risp ="KO"
                        risultato = "Studente già inserito"

                elif comando == "#put":
                    studente = parametri[0]
                    materia = parametri[1]
                    voti = parametri[2]
                    ore = parametri[3]
                    
                    if studente in diz:
                        diz[studente][materia]=voti
                        risp = "OK"
                        risultato = "voti inseriti"
                    else:
                        risp ="KO"
                        risultato="Studente non presente"

                dati = {"risposta":risp,
                        "valori":risultato,
                }

                    
                sock.sendall((str(dati)).encode())

