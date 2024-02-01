import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

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

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((SERVER_IP,SERVER_PORT))
    sock.listen()
    print(f"Server in ascolto su {SERVER_IP}:{SERVER_PORT}...")

    while True:
        sock_service, address_client = sock.accept()
        
        with sock_service as sock_client:
            while True:
                istruzioni = sock_client.recv(BUFFER_SIZE).decode()
                if not istruzioni:
                    break
                
                istruzioni = json.loads(istruzioni)
                
                comando = (istruzioni["comando"]).split("#")[1]
                parametri = (istruzioni["parametri"])
            
                

                
                
                parametri = (istruzioni["parametri"]).split("/")
                print(parametri)
                
                if comando == "list":
                    risp = "OK"
                    risultato = diz
                
                elif comando == "get":
                    studente = parametri[1]  # Accedi all'elemento corretto della lista
                    if studente in diz:
                        risp = "OK"
                        risultato = diz[studente]
                    else:
                        risp = "KO"
                        risultato = "Studente non presente"

                elif comando == "set":
                    studente = tuple(parametri)  # Converte la lista in una tupla
                    print("Parametri:", studente)

                    if studente not in diz:
                        diz[studente] = {}
                        risp = "OK"
                        risultato = "Studente inserito"
                    else:
                        risp = "KO"
                        risultato = "Studente già inserito"

                    print("Dizionario dopo l'operazione di set:", diz)

                elif comando == "put":
                    studente = parametri[1]
                    materia = parametri[2]
                    voti = parametri[3]
                    ore = parametri[4]

                    print(studente,materia,voti,ore)
                    
                        
                    if studente in diz:
                        diz[studente] = [materia,voti,ore]
                        risp = "OK"
                        risultato = "Voti inseriti"
                    else:
                        risp = "KO"
                        risultato = "Studente non presente"
                        
                    print(risp)
                    print(risultato)
                    
                dati = {"risposta":risp,
                        "valori":risultato,
                }

                    
                sock_service.sendall((str(dati)).encode())

