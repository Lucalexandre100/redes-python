# coding: utf-8

# In[ ]:


# CRIANDO UM SERVIDOR PYTHON
import socket
from datetime import *
 
host = '127.0.0.1'      # o mesmo que localhost
porta = 8080            # porta da conexão
 
soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #estou usando TCP/IP
recebe = (host, porta)
soquete.bind(recebe)
soquete.listen(2)
 
print('\nSERVIDOR INICIADO...IP: ', host, 'PORTA: ', porta,' EM: ',datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
 
while True:
    conexao, enderecoIP = soquete.accept()
    print('\nSERVIDOR ACESSADO PELO CLIENTE:', enderecoIP, 'EM: ',datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
 
    while True:
        mensagem = conexao.recv(2048)
        if not mensagem:
            break
        print('\nIP CLIENTE:', enderecoIP)
        print('MENSAGEN RECEBIDA: ', mensagem.decode(),' - ',datetime.now().strftime('%H:%M:%S'))
        conexao.sendall(b'Hello world!')
        break
 
    print('CONEXÃO COM O CLIENTE FINALIZADA...', enderecoIP, ' EM: ',datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
    conexao.close()

# --------------------------------------- Cliente ---------------------------------------


# coding: utf-8

# In[18]:



# coding: utf-8

# In[1]:


# criando um cliente para conexão com o servidor Python
import socket
import sys
import os
 
host = '127.0.0.1'  # mesmo local do servidor
porta = 8080        # mesma porta do servidor
 
envio = (host,porta)

print(envio)

'''
soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soquete.connect(envio)
 
print('Digite: S e pressione ENTER para encerrar...') 
print('DIGITE A MENSAGEM: ')
mensagem = input()
 
while mensagem not in ('s','S'):
    soquete.send(str(mensagem).encode())
    mensagem = input()
    
soquete.close()    
'''

i = 0
for i in range(i==0):
    print(i)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(envio)
    print (f">> GET / {porta} HTTP/1.1")
    s.send(f"GET / {porta}  HTTP1.1\r\n".encode())
    s.send(f"HOST: {host} /r/n/r/n".encode());

    while True:
        msg = s.recv(2048)
        if not msg:
            break
        print(msg)

    s.close()


#https://www.youtube.com/watch?v=7vjO8lP3EtE

