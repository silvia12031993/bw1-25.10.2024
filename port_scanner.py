import socket

target_scan = input("Inserisci l'indirizzo IP del dispositivo che vuoi scansionare: ")
porta_iniziale = int(input("Inserisci la porta iniziale (es. 1): "))
porta_finale = int(input("Inserisci la porta finale (es. 1024): "))

print("Scansione di ", target_scan, "dalla porta ", porta_iniziale, "alla porta ", porta_finale)

for porta in range(porta_iniziale, porta_finale):
    connessione = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = connessione.connect_ex((target_scan, porta))
    if status == 0:
        print("+*+ Porta ", porta, " APERTA +*+")
    connessione.close();
