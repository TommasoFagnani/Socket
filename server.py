import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

#Creazione del socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((SERVER_IP,SERVER_PORT))

print("Server in attesa di messaggio...")

while True:
    data,addr = sock.recvfrom(1024)
    if not data:
        break
    data = data.decode()
    data = json.loads(data)
    print(data)
    primoNumero = data["primoNumero"]
    operazione = data["operazione"]
    secondoNumero = data["secondoNumero"]

    #Calcoliiiii!!!!
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
    sock.sendto(str(risultato).encode(), addr)

#sock.close()