import socket                   # Importa el mÃ³dulo Socket
import sys
import string
s = socket.socket()             # Crea el objeto socket
host = "localhost"    # Obtiene el nombre de la PC local
port = 60000                 # Reserva un PUERTO para el servicio
s.connect((host, port))
data = s.recv(1024).decode()
strings = str(data)
num = int(strings)
dato= s.recv(1024).decode()
stringkey= str(dato)
key= int(stringkey)
print(num)
print(key)

def Encrypt (msg, shift):
    chars = " " + string.punctuation + string.digits + string.ascii_letters             #Todos los caracteres admitidos en nuestro codigo                                                               #se cambia las caracteristicas de char, de string a lista
    shift %= len(chars)

    key = chars[shift:] + chars[:shift]                                                 #Tomas caracteres del inicio y los mandas al final
    table = str.maketrans(chars, key)                                                   #Una tabla de traduccion que se usara en el sgte mensaje
    crypted = msg.translate(table)                                                      #Usas la tabla de traduccion para traducir el msg
    return crypted
def Decrypt (crypted, shift):                                                         #igual q el otro tbh, solo cambia 1 paso, que es invertir el codigo para q el mensaje tmbn se revierta
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    shift %= len(chars)

    key =  chars[-shift:] + chars[:-shift]                                              #Tomas caracteres del final y los pones en el inicio
    table = str.maketrans(chars, key)                                                  
    decrypted = crypted.translate(table)                
    return decrypted


if num ==0:
    print('Eres el primer cliente') 
    while True:
        
        mensaje = input(">>>")
        if mensaje != 'adios':
            mensaje = Encrypt(mensaje, key)
            s.send(mensaje.encode())

            respuesta = s.recv(4096).decode()
            print('Crypted: '+ respuesta)
            respuesta = Decrypt(respuesta, key)
            print('Decrypted: '+ respuesta)
            if respuesta == 'adios':
                print('Se termino la conexion.')
                s.close()
                sys.exit()
            
        else:
            mensaje = Encrypt(mensaje, key)
            s.send(mensaje.encode())
            s.close()
            sys.exit()

else:
    print('Eres el segundo cliente')    
    while True:
        respuesta = s.recv(4096).decode()
        print('Crypted: '+respuesta)
        respuesta = Decrypt(respuesta, key)
        print('Decrypted: '+ respuesta)
        if respuesta == 'adios':
                print('Se termino la conexion.')
                s.close()
                sys.exit()

        mensaje = input(">>>")
        if mensaje != 'adios':
            mensaje = Encrypt(mensaje, key)
            s.send(mensaje.encode())

        else:
            mensaje = Encrypt(mensaje, key)
            s.send(mensaje.encode())
            s.close()
            sys.exit()
