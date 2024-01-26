import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 22007
BUFFER_SIZE = 1024


print("Server in attesa di messaggio...")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
    sock_server.bind((SERVER_IP,SERVER_PORT))
    sock_server.listen()
    print(f"Server in ascolto su {SERVER_IP}:{SERVER_PORT}...")
    while True:
        sock_service, address_client = sock_server.accept()
        
        with sock_service as sock_client:
            while True:
                data=sock_client.recv(BUFFER_SIZE).decode()
                if not data:
                    break
                data = json.loads(data)
            
                primoNumero = data["primoNumero"]
                operazione = data["operazione"]
                secondoNumero = data["secondoNumero"]

                risultato = 0
                if operazione == '+':
                        risultato = primoNumero + secondoNumero
                elif operazione == '-':
                        risultato = primoNumero - secondoNumero
                elif operazione == '*':
                        risultato = primoNumero * secondoNumero
                elif operazione == '/':
                    if secondoNumero != 0:
                        risultato = primoNumero / secondoNumero
                    else:
                        "impossibile dividere per 0!"
                elif operazione == '%':
                    risultato = primoNumero % secondoNumero

                sock_service.sendall((str(risultato)).encode())
                

        
