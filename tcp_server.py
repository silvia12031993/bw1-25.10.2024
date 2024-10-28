import socket

ip_server = str(input("Inserisci l'IP del server: "))
port_server = input("Inserisci la porta del server (default: 44444): ")
if  port_server == '':
    port_server = 44444

socket_address = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ipv4, protocollo
socket_address.bind((ip_server, int(port_server)))
socket_address.listen(1) #va in ascolto, massimo 1 connessione per volta

print("Il server è in ascolto... In attesa di connessione...")
connection, ip_client = socket_address.accept() #accetta la connessione del client
print("Client connesso con IP ", ip_client)

while 1: # finché il client invia dati
    data = connection.recv(1024) #ricevi i dati
    if not data: break
    print("Dati ricevuti.")
    print(data.decode('utf-8')) #decodifica e stampa i dati ricevuti
connection.close()
