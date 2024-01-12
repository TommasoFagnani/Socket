import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    primoNumero = float(input("Inserisci il primo numero: "))
    operazione = input("Inserisci l'operazione (+, -, *, /, 8%): ")
    secondoNumero = float(input("Inserisci il secondo numero: "))
    messaggio = {
        "primoNumero":primoNumero,
        "operazione":operazione,
        "secondoNumero":secondoNumero
    }
    messaggio = json.dumps(messaggio)
    sock.sendto(messaggio.encode("UTF-8"),(SERVER_IP, SERVER_PORT))
    data = sock.recv(1024)
    print("Risultato:", data.decode())

#chiusura socket
#sock.close()