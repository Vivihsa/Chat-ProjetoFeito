from http import client
import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#SOCK_STREAM:  faz A comunicação entre os streams (o cliente e servidor)
#F_INET:  para utilizar procotolO TCP/IP
servidor.bind(('localhost', 8889)) 
# para vincular o endereço do servidor


servidor.listen() 
# escutar as conexões que está sendo chamado/requisitado
cliente , end = servidor.accept() # aceitar as conexões

terminado = False # para entrar em loop infinito


while not terminado:
    msg = cliente.recv(1024).decode('utf-8')
    if msg == 'tt':
        terminado = True
    else:
        print(f'Recebido: {msg}')
    cliente.send(input('Mensagem: ').encode('utf-8'))

cliente.close()
servidor.close()