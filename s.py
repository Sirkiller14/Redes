import socket                   # Importa el mÃ³dulo Socket
import random
port = 60000                   # Reserva un PUERTO para el servicio
s = socket.socket()             # Crea un objeto socket
s.bind(('', port))            # Lo enlaza al puerto
s.listen()                     # Espera por la conexiÃ³n de un Cliente
key = random.randint(1,100)
print ('Servidor escuchando ...')

while True:
    
    conn1, addr = s.accept()     # Establece conexiÃ³n con el Cliente
    print ('Conectado con un cliente ', addr)
    conn1.send(bytes(str(0), 'utf8'))
    conn1.send(bytes(str(key), 'utf8'))
    conn2, addr = s.accept()     # Establece conexiÃ³n con el Cliente
    print ('Conectado con un cliente ', addr)
    conn2.send(bytes(str(1), 'utf8'))
    conn2.send(bytes(str(key), 'utf8'))
    

    while True:
        
        mensaje1= conn1.recv(4096).decode()
        if mensaje1 != '':
            print("Cliente1:"+ mensaje1)
            conn2.send(mensaje1.encode())
        mensaje2= conn2.recv(4096).decode()
        if mensaje2 != '':
            print("Cliente2:"+ mensaje2)
            conn1.send(mensaje2.encode())
         

        if mensaje1 == 'adios' or mensaje2== 'adios':
            break
        
        

    print('Desconectado el cliente')
    conn1.close()
    conn2.close()
